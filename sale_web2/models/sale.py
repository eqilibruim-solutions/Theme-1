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
import odoorpc


class Partner(models.Model):
	
	_inherit = "res.partner"
	
	customer_id = fields.Char("CUSTOMER ID")
	
	

class sale_order(models.Model):
	
	_inherit = "sale.order"
	
	moved = fields.Boolean("Moved")
	
	
	def write(self, vals):
		
		res = super(sale_order, self).write(vals)
		
		if 'access_token' in vals:
			self.action_synch_so()
		
		return res
	
	
		
	
	def action_synch_so(self):
		
		ICP_obj = self.env['ir.config_parameter'].sudo()
		url = ICP_obj.get_param('sync_url')
		user1 = ICP_obj.get_param('sync_user')
		pwd = ICP_obj.get_param('sync_pwd')
		db = ICP_obj.get_param('sync_db')
		port1 = ICP_obj.get_param('sync_port')
		
		
		for order in self.search([('moved', '=', False), ('state', 'not in', ['draft', 'cancel'])]):
			
			
			remote_odoo = odoorpc.ODOO(url, port=port1)
			remote_odoo.login(db, user1, pwd)
			
			Partner_r = remote_odoo.env['res.partner']
			User_r = remote_odoo.env['res.users']
			Order_r = remote_odoo.env['sale.order']
			Order_Line_r = remote_odoo.env['sale.order.line']
			Pricelist_r = remote_odoo.env['product.pricelist']
			Payment_Term_r = remote_odoo.env['account.payment.term']
			Crm_Team_r = remote_odoo.env['crm.team']
			Website_r = remote_odoo.env['website']
			Product_r = remote_odoo.env['product.product']
			
			print (remote_odoo.env.db, 'DDDDDDDDDDDDDDDDDDD')
			
			local_partner_id = self.partner_id
			remote_partner_id = Partner_r.search(['|', ('email', '=', local_partner_id.email), ('customer_id', '=', local_partner_id.customer_id)], limit=1)
			if not remote_partner_id:
				remote_partner_id = Partner_r.create({
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
											})
			else: remote_partner_id = remote_partner_id[0]
											
			local_pricelist_id = order.pricelist_id
			remote_pricelist_id = False
			if local_pricelist_id:
				remote_pricelist_id = Pricelist_r.search([('name', '=', local_pricelist_id.name)], limit=1)
				if remote_pricelist_id:
					remote_pricelist_id = remote_pricelist_id[0]
				
			
			local_payment_term_id = order.payment_term_id
			remote_payment_term_id = False
			if local_payment_term_id:
				remote_payment_term_id = Payment_Term_r.search([('name', '=', local_payment_term_id.name)], limit=1)
				if remote_payment_term_id:
					remote_payment_term_id = remote_payment_term_id[0]
				else:
					remote_payment_term_id = Payment_Term_r.create({
																	'name': local_payment_term_id.name,
																	})
																		
																		
																		
			local_team_id = order.team_id
			remote_team_id = False
			if local_team_id:
				remote_team_id = Crm_Team_r.search([('name', '=', local_team_id.name)], limit=1)
				if remote_team_id:
					remote_team_id = remote_team_id[0]
				else:
					remote_team_id = Crm_Team_r.create({
													'name': local_team_id.name,
													})
													
													
			local_user_id = order.user_id
			remote_user_id = False
			if local_user_id:
				remote_user_id = User_r.search([('email', '=', local_user_id.email)], limit=1)
				if remote_user_id:
					remote_user_id = remote_user_id[0]
				else:
					user_local_partner_id = local_user_id.partner_id
					user_remote_partner_id = Partner_r.search(['|', ('email', '=', user_local_partner_id.email), ('customer_id', '=', user_local_partner_id.customer_id)], limit=1)
					if not user_remote_partner_id:
						user_remote_partner_id = Partner_r.create({
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
													})
					else:user_remote_partner_id = user_remote_partner_id[0]
						
					remote_user_id = User_r.create({
													'name': local_user_id.name,
													'email': local_user_id.email,
													'partner_id': user_remote_partner_id,
													})
																		
																		
																		
			local_website_id = order.website_id
			remote_website_id = False
			if local_website_id:
				remote_website_id = Website_r.search([('name', '=', local_website_id.name)], limit=1)
				if remote_website_id:
					remote_website_id = remote_website_id[0]
				else:
					remote_website_id = Website_r.create({
													'name': local_website_id.name,
													})
													
													
													
		
			so_val = {
				'partner_id': remote_partner_id, 
				'pricelist_id': remote_pricelist_id, 
				'payment_term_id': remote_payment_term_id, 
				'team_id': remote_team_id, 
				'partner_invoice_id': remote_partner_id, 
				'partner_shipping_id': remote_partner_id, 
				'user_id': remote_user_id, 
				'website_id': remote_website_id, 
				'company_id': 1, 
				#'plain_date': order.plain_date, 
				#'unique_seq': order.unique_seq
				}
		
			so_id = Order_r.create(so_val)
			
			print ('\n', so_id, 'SO created...')
		
			for item in order.order_line:
				local_product_id = item.product_id
				remote_product_id = False
				if local_product_id:
					remote_product_id = Product_r.search([('default_code', '=', local_product_id.default_code)], limit=1)
					if remote_product_id:
						remote_product_id = remote_product_id[0]
					else:
						remote_product_id = Product_r.create({
														'name': local_product_id.name,
														'default_code': local_product_id.default_code,
														'type': local_product_id.type,
														})
						
														
				sol_val = {
					'product_id': remote_product_id, 
					'product_uom_qty': 1, 
					'order_id': so_id, 
					'product_uom': 1, 
					'price_unit': item.price_unit, 
					'discount': item.discount,
					}
					
				
				sol_id = Order_Line_r.create(sol_val)
				print ('SOL', sol_id, 'SOL created...')
		
		
			order.moved = True
			self._cr.commit()

				

















		
		
