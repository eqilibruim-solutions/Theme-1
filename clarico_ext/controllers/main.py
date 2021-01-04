# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import odoo
from odoo import http, SUPERUSER_ID, api, tools
from odoo.http import request
import json
from odoo.addons.website_sale.controllers.main import WebsiteSale
import io
import csv
import base64
from odoo.tools import pycompat
from odoo.exceptions import UserError, AccessError, ValidationError
from psycopg2 import IntegrityError

from odoo.addons.mail.models.mail_message import Message
from odoo.addons.website.controllers.main import Website


	
	
# @http.route('/', type='http', auth="public", website=True)
# def index(self, **kw):
# 	homepage = request.website.homepage_id
# 	if homepage and (homepage.sudo().is_visible or request.env.user.has_group('base.group_user')) and homepage.url != '/':
# 		return request.env['ir.http'].reroute(homepage.url)
# 
# 	return request.render('/', {})
# 	
# 	website_page = request.env['ir.http']._serve_page()
# 	if website_page:
# 		return website_page
# 	else:
# 		top_menu = request.website.menu_id
# 		first_menu = top_menu and top_menu.child_id and top_menu.child_id.filtered(lambda menu: menu.is_visible)
# 		if first_menu and first_menu[0].url not in ('/', '', '#') and (not (first_menu[0].url.startswith(('/?', '/#', ' ')))):
# 			return request.redirect(first_menu[0].url)
# 
# 	raise request.not_found()
# 
# 
# Website.index = index	


class WebsiteSale2(WebsiteSale):
	
	@http.route(['/shop/cart/update'], type='http', auth="public", methods=['GET', 'POST'], website=True,
			csrf=False)
	def cart_update(self, product_id, add_qty=1, set_qty=0, **kw):
		sale_order = request.website.sale_get_order(force_create=True)
		if sale_order.state != 'draft':
			request.session['sale_order_id'] = None
			sale_order = request.website.sale_get_order(force_create=True)

		product_custom_attribute_values = None
		if kw.get('product_custom_attribute_values'):
			product_custom_attribute_values = json.loads(kw.get('product_custom_attribute_values'))

		no_variant_attribute_values = None
		if kw.get('no_variant_attribute_values'):
			no_variant_attribute_values = json.loads(kw.get('no_variant_attribute_values'))

		if 'uom_id' in kw:
			sale_order._cart_update(
				product_id=int(product_id),
				add_qty=add_qty,
				set_qty=set_qty,
				product_uom_id= int(kw['uom_id']),
				product_custom_attribute_values=product_custom_attribute_values,
				no_variant_attribute_values=no_variant_attribute_values
			)
		else:
			sale_order._cart_update(
				product_id=int(product_id),
				add_qty=add_qty,
				set_qty=set_qty,
				product_custom_attribute_values=product_custom_attribute_values,
				no_variant_attribute_values=no_variant_attribute_values
			)

#		 if kw.get('express'):
#			 return request.redirect("/shop/checkout?express=1")

		return request.redirect("/shop/cart")
	   
	   
	   


	   	
	
class EmiproThemeBase(http.Controller):
	
	@http.route(['/get_uom_price'], type='json', auth="public", website=True)
	def get_uom_price(self, **kw):
		
		uom = request.env['uom.uom'].sudo().browse(int(kw['uom']))
		factor = uom.factor_inv
		ref = uom.uom_type
		
		price = float(kw['price'])
		if ref == 'bigger':
			price = price * factor
		if ref == 'smaller':
			price = price / factor
		
		return json.dumps({'price': price})
	
	
	
	
		   
		   
		   
		   
		   
		   
		   
		   
		   
	
	
	
