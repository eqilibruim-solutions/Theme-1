# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, tools, _
from odoo import SUPERUSER_ID
import io
import csv
import base64
import ftplib
from odoo.tools import pycompat
from odoo.exceptions import UserError, AccessError

from odoo.addons.website_mail.models.mail_message import MailMessage
from datetime import datetime, timedelta
from itertools import chain
from odoo.addons.product.models.product_pricelist import Pricelist



def _compute_price_rule(self, products_qty_partner, date=False, uom_id=False):
	""" Method monkey patched to change code according to customer selection in pricelist
	"""
	print ('Computing price......................')
	self.ensure_one()
	if not date:
		date = self._context.get('date') or fields.Date.today()
	date = fields.Date.to_date(date)  # boundary conditions differ if we have a datetime
	if not uom_id and self._context.get('uom'):
		uom_id = self._context['uom']
	if uom_id:
		# rebrowse with uom if given
		products = [item[0].with_context(uom=uom_id) for item in products_qty_partner]
		products_qty_partner = [(products[index], data_struct[1], data_struct[2]) for index, data_struct in enumerate(products_qty_partner)]
	else:
		products = [item[0] for item in products_qty_partner]

	if not products:
		return {}

	categ_ids = {}
	for p in products:
		categ = p.categ_id
		while categ:
			categ_ids[categ.id] = True
			categ = categ.parent_id
	categ_ids = list(categ_ids)

	is_product_template = products[0]._name == "product.template"
	if is_product_template:
		prod_tmpl_ids = [tmpl.id for tmpl in products]
		# all variants of all products
		prod_ids = [p.id for p in
					list(chain.from_iterable([t.product_variant_ids for t in products]))]
	else:
		prod_ids = [product.id for product in products]
		prod_tmpl_ids = [product.product_tmpl_id.id for product in products]

	items = self._compute_price_rule_get_items(products_qty_partner, date, uom_id, prod_tmpl_ids, prod_ids, categ_ids)

	results = {}
	for product, qty, partner in products_qty_partner:
		results[product.id] = 0.0
		suitable_rule = False

		# Final unit price is computed according to `qty` in the `qty_uom_id` UoM.
		# An intermediary unit price may be computed according to a different UoM, in
		# which case the price_uom_id contains that UoM.
		# The final price will be converted to match `qty_uom_id`.
		qty_uom_id = self._context.get('uom') or product.uom_id.id
		price_uom_id = product.uom_id.id
		qty_in_product_uom = qty
		if qty_uom_id != product.uom_id.id:
			try:
				qty_in_product_uom = self.env['uom.uom'].browse([self._context['uom']])._compute_quantity(qty, product.uom_id)
			except UserError:
				# Ignored - incompatible UoM in context, use default product UoM
				pass

		# if Public user try to access standard price from website sale, need to call price_compute.
		# TDE SURPRISE: product can actually be a template
		price = product.price_compute('list_price')[product.id]

		price_uom = self.env['uom.uom'].browse([qty_uom_id])
		for rule in items:
			if rule.min_quantity and qty_in_product_uom < rule.min_quantity:
				continue
			if is_product_template:
				if rule.product_tmpl_id and product.id != rule.product_tmpl_id.id:
					continue
				if rule.product_id and not (product.product_variant_count == 1 and product.product_variant_id.id == rule.product_id.id):
					# product rule acceptable on template if has only one variant
					continue
			else:
				if rule.product_tmpl_id and product.product_tmpl_id.id != rule.product_tmpl_id.id:
					continue
				if rule.product_id and product.id != rule.product_id.id:
					continue

			if rule.categ_id:
				cat = product.categ_id
				while cat:
					if cat.id == rule.categ_id.id:
						break
					cat = cat.parent_id
				if not cat:
					continue

			if rule.base == 'pricelist' and rule.base_pricelist_id:
				price_tmp = rule.base_pricelist_id._compute_price_rule([(product, qty, partner)], date, uom_id)[product.id][0]  # TDE: 0 = price, 1 = rule
				price = rule.base_pricelist_id.currency_id._convert(price_tmp, self.currency_id, self.env.company, date, round=False)
			else:
				# if base option is public price take sale price else cost price of product
				# price_compute returns the price in the context UoM, i.e. qty_uom_id
				price = product.price_compute(rule.base)[product.id]

			convert_to_price_uom = (lambda price: product.uom_id._compute_price(price, price_uom))

			if price is not False:
				if rule.compute_price == 'fixed':
					price = convert_to_price_uom(rule.fixed_price)
				elif rule.compute_price == 'percentage':
					price = (price - (price * (rule.percent_price / 100))) or 0.0
				else:
					# complete formula
					price_limit = price
					price = (price - (price * (rule.price_discount / 100))) or 0.0
					if rule.price_round:
						price = tools.float_round(price, precision_rounding=rule.price_round)

					if rule.price_surcharge:
						price_surcharge = convert_to_price_uom(rule.price_surcharge)
						price += price_surcharge

					if rule.price_min_margin:
						price_min_margin = convert_to_price_uom(rule.price_min_margin)
						price = max(price, price_limit + price_min_margin)

					if rule.price_max_margin:
						price_max_margin = convert_to_price_uom(rule.price_max_margin)
						price = min(price, price_limit + price_max_margin)
				suitable_rule = rule
				
				## CUSTOM CODE FOR STATES
				rule = self.env['product.pricelist.item'].sudo().browse(rule.id)
				states = rule.state_ids_pricelist.ids
				
				current_user = self.env['res.users'].sudo().browse(self._uid) 
				if self._uid and states and current_user.partner_id.state_id.id not in states:
					price = product.list_price
					
					
				## CUSTOM CODE FOR CUSTOMER
				rule = self.env['product.pricelist.item'].sudo().browse(rule.id)
				userss = rule.user_ids.ids
				if self._uid and userss and self._uid not in userss:
					price = product.list_price
					
					
			
			break
		# Final price conversion into pricelist currency
		if suitable_rule and suitable_rule.compute_price != 'fixed' and suitable_rule.base != 'pricelist':
			if suitable_rule.base == 'standard_price':
				cur = product.cost_currency_id
			else:
				cur = product.currency_id
			price = cur._convert(price, self.currency_id, self.env.company, date, round=False)

		if not suitable_rule:
			cur = product.currency_id
			price = cur._convert(price, self.currency_id, self.env.company, date, round=False)

		results[product.id] = (price, suitable_rule and suitable_rule.id or False)

	
	return results
	   
	   
	   
	   		
Pricelist._compute_price_rule = _compute_price_rule		

	
		
	
class PricelistItem(models.Model):
	_inherit = "product.pricelist.item"
	
	user_ids = fields.Many2many('res.users', 'user_pricelist_item_rel1',
									 'user_id', 'pricelist_id', string='Customer')
	
	
	state_ids_pricelist = fields.Many2many('res.country.state', 'state_pricelist_item_rel1',
									 'state_id', 'pricelist_id', string='States/Provinces')
	
		
		
		
		
