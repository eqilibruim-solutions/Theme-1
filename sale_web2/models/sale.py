# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, tools, _
from odoo import SUPERUSER_ID
import io
import csv
import base64
import ftplib
import odoo
from odoo.exceptions import UserError, AccessError



class sale_order(models.Model):
	
	_inherit = "sale.order"
	
	moved = fields.Boolean("Moved")
	
	def action_synch_so(self):
		
		for order in self.search([('moved', '=', False), ('state', 'not in', ['draft', 'cancel'])]):
			
			
			db_name = 'test13ent'
			registry = odoo.registry(db_name)
			with registry.cursor() as cr:
				env = api.Environment(cr, SUPERUSER_ID, {})
				
				
				local_partner_id = self.partner_id
				remote_partner_id = env['res.partner'].search(['|', ('email', '=', local_partner_id.email), ('customer_id', '=', local_partner_id.customer_id)], limit=1)
				if not remote_partner_id:
					remote_partner_id = env['res.partner'].create({
												'name': local_partner_id.name,
												'email': local_partner_id.email or '',
												'customer_id': local_partner_id.customer_id or '',
												'street': local_partner_id.street or '',
												'street2': local_partner_id.street2 or '',
												'zip': local_partner_id.zip or '',
												'city': local_partner_id.city or '',
												'phone': local_partner_id.phone or '',
												'mobile': local_partner_id.mobile or '',
												'company_type': local_partner_id.company_type,
												}).id
												
				local_pricelist_id = order.pricelist_id
				remote_pricelist_id = False
				if local_pricelist_id:
					remote_pricelist_id = env['product.pricelist'].search([('name', '=', local_pricelist_id.name)], limit=1)
					if remote_pricelist_id:
						remote_pricelist_id = remote_pricelist_id.id
					
				
				local_payment_term_id = order.payment_term_id
				remote_payment_term_id = False
				if local_payment_term_id:
					remote_payment_term_id = env['account.payment.term'].search([('name', '=', local_payment_term_id.name)], limit=1)
					if remote_payment_term_id:
						remote_payment_term_id = remote_payment_term_id.id
					else:
						remote_payment_term_id = env['account.payment.term'].create({
																			'name': local_payment_term_id.name,
																			}).id
																			
																			
																			
				local_team_id = order.team_id
				remote_team_id = False
				if local_team_id:
					remote_team_id = env['crm.team'].search([('name', '=', local_team_id.name)], limit=1)
					if remote_team_id:
						remote_team_id = remote_team_id.id
					else:
						remote_team_id = env['crm.team'].create({
														'name': local_team_id.name,
														}).id
														
														
				local_user_id = order.user_id
				remote_user_id = False
				if local_user_id:
					remote_user_id = env['res.users'].search([('email', '=', local_user_id.email)], limit=1)
					if remote_user_id:
						remote_user_id = remote_user_id.id
					else:
						user_local_partner_id = local_user_id.partner_id
						user_remote_partner_id = env['res.partner'].search(['|', ('email', '=', user_local_partner_id.email), ('customer_id', '=', user_local_partner_id.customer_id)], limit=1)
						if not user_remote_partner_id:
							user_remote_partner_id = env['res.partner'].create({
														'name': user_local_partner_id.name,
														'email': user_local_partner_id.email or '',
														'customer_id': user_local_partner_id.customer_id or '',
														'street': user_local_partner_id.street or '',
														'street2': user_local_partner_id.street2 or '',
														'zip': user_local_partner_id.zip or '',
														'city': user_local_partner_id.city or '',
														'phone': user_local_partner_id.phone or '',
														'mobile': user_local_partner_id.mobile or '',
														'company_type': user_local_partner_id.company_type,
														}).id
						remote_user_id = env['res.users'].create({
														'name': local_user_id.name,
														'email': local_user_id.email,
														'partner_id': user_remote_partner_id.id,
														}).id
																			
																			
																			
				local_website_id = order.website_id
				remote_website_id = False
				if local_website_id:
					remote_website_id = env['website'].search([('name', '=', local_website_id.name)], limit=1)
					if remote_website_id:
						remote_website_id = remote_website_id.id
					else:
						remote_website_id = env['website'].create({
														'name': local_website_id.name,
														}).id
														
														
														
			
				so_val = {
					'partner_id': remote_partner_id.id, 
					'pricelist_id': remote_pricelist_id, 
					'payment_term_id': remote_payment_term_id, 
					'team_id': remote_team_id, 
					'partner_invoice_id': remote_partner_id.id, 
					'partner_shipping_id': remote_partner_id.id, 
					'user_id': remote_user_id, 
					'website_id': remote_website_id, 
					'company_id': 1, 
					'plain_date': order.plain_date, 
					'unique_seq': order.unique_seq
					}
			
				so_id = env['sale.order'].create(so_val)
				
				print ('\n', so_id, 'SO created...')
			
				for item in order.order_line:
					local_product_id = item.product_id
					remote_product_id = False
					if local_product_id:
						remote_product_id = env['product.product'].search([('default_code', '=', local_product_id.default_code)], limit=1)
						if remote_product_id:
							remote_product_id = remote_product_id.id
						else:
							remote_product_id = env['product.product'].create({
															'name': local_product_id.name,
															'default_code': local_product_id.default_code,
															'type': local_product_id.type,
															}).id
							
															
					sol_val = {
						'product_id': remote_product_id, 
						'product_uom_qty': 1, 
						'order_id': so_id.id, 
						'product_uom': 1, 
						'price_unit': item.price_unit, 
						'discount': item.discount,
						}
						
					
					sol_id = env['sale.order.line'].create(sol_val)
					print ('        ', sol_id, 'SOL created...')
		
		
			order.moved = True
			self._cr.commit()

				

















		
		
