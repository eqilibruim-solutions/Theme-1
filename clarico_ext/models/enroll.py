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

from odoo.addons.website_sale.models.sale_order import SaleOrder


class enroll_partner(models.Model):
	
	_name = 'enroll.partner'
	_rec_name ='c_name'
	
	
	
	def action_approve(self):
		self.ensure_one()
		
		state_id = self.env['res.country.state'].sudo().search([('name', '=', self.b_state)])
		if state_id:
			state_id = state_id.id
		else:
			state_id = False
			
		
		country_id = self.env['res.country'].sudo().search([('name', '=', self.b_country)])
		if country_id:
			country_id = country_id.id
		else:
			country_id = False
			
			
		
		val = {
			'name': self.c_name,
			'email': self.c_email,
			'phone': self.c_phone,
			'street': self.b_street,
			'street2': self.b_street2,
			'city': self.b_city,
			'zip': self.b_zip,
			'state_id': state_id,
			'country_id': country_id,
			}
		
		self.env['res.partner'].sudo().create( val )
		
		
		
		self.state = 'approve'
		
		
		
	def action_deny(self):
		self.ensure_one()
		self.state = 'deny'
	
	state = fields.Selection([('draft', 'Draft'), ('approve', 'Approved'), ('deny', 'Denied')], default="draft")
	
	#TAB 1 CUSTOMER DETAILS
	c_name = fields.Char("Company Name")
	c_phone = fields.Char("Telephone")
	c_fax = fields.Char("Fax")
	c_email = fields.Char("Email")
	
	b_street = fields.Char("Street")
	b_street2 = fields.Char("Street2")
	b_city = fields.Char("City")
	b_zip = fields.Char("Zip")
	b_state = fields.Char("State")
	b_country = fields.Char("Country")
	
	s_street = fields.Char("Street")
	s_street2 = fields.Char("Street2")
	s_city = fields.Char("City")
	s_zip = fields.Char("Zip")
	s_state = fields.Char("State")
	s_country = fields.Char("Country")
	dir_name1 = fields.Char("Director1")
	dir_phone1 = fields.Char("Phone")
	dir_name2 = fields.Char("Director2")
	dir_phone2 = fields.Char("Phone")
	dir_name3 = fields.Char("Director3")
	dir_phone3 = fields.Char("Phone")
	dir_name4 = fields.Char("Director4")
	dir_phone4 = fields.Char("Phone")
	contact_person = fields.Char("Contact Person")
	dunn_no = fields.Char("Dunn & Bradstreet #")
	
	cred_name1 = fields.Char("Credit References1")
	cred_phone1 = fields.Char("Phone")
	cred_addr1 = fields.Char("Address")
	cred_name2 = fields.Char("Credit References2")
	cred_phone2 = fields.Char("Phone")
	cred_addr2 = fields.Char("Address")
	cred_name3 = fields.Char("Credit References3")
	cred_phone3 = fields.Char("Phone")
	cred_addr3 = fields.Char("Address")
	cred_name4 = fields.Char("Credit References4")
	cred_phone4 = fields.Char("Phone")
	cred_addr4 = fields.Char("Address")
	
	service_acc_no = fields.Char("How many accounts do you service?")
	year_no = fields.Char("How long have you been in business?")
	stamp_state_names = fields.Char("Are you a stamping authority? If yes, which states?")
	employee_no = fields.Char("Number of Employees?")
	sales_vol = fields.Char("Sales volume for last year?")
	business_state_names = fields.Char("Which states are you doing business in?")
	activity_report_yes_no = fields.Char("Are you able to provide an activity report?")
	stamp_product_yes_no = fields.Char("Are you able to receive stamped product?")
	eft_yes_no = fields.Char("Will you be able to operate with EFT (Electronic Funds Transfer) as a payment option?")
	signature_whole = fields.Binary("Signature (Wholesaler)")
	signature_date = fields.Date("Date",default=fields.Date.context_today)
	void_check = fields.Binary("Attach a VOID CHECK here")
	
	#TAB 2 BANK REFERENCE REQUEST
	client_name = fields.Char("Client Name")
	client_bank = fields.Char("Bank Name")
	client_account = fields.Char("Account Number")
	client_phone = fields.Char("Phone")
	client_email = fields.Char("Email")
	client_date = fields.Char("Date")
	client_name_customer = fields.Char("Name of Customer")
	client_signature = fields.Binary("Client Signature")
	client_customer_aod = fields.Date("Date of Account Opening",default=fields.Date.context_today)
	client_name_customer_bank_off_sig = fields.Binary("Bank Officers Signature")
	
	
	#Tab 3 AGREEMENT for EFT TRANSACTION 
	aggreement_company_name = fields.Char("Company Name")
	aggreement_street = fields.Char("Street")
	aggreement_company_city = fields.Char("City")
	aggreement_company_state = fields.Char("State")
	aggreement_company_zip = fields.Char("Zip")
	aggreement_company_phone = fields.Char("Phone")
	aggreement_company_fax = fields.Char("Fax")
	aggreement_institute_name = fields.Char("Financial Institution Name")
	aggreement_branch = fields.Char("Branch")
	aggreement_address = fields.Char("Address")
	aggreement_route_no = fields.Char("Routing No.")
	aggreement_account_no = fields.Char("Account Number")
	aggreement_account_type = fields.Char("Type of Account")
	aggreement_bottom_name = fields.Char("Agreement Name")
	aggreement_bottom_title = fields.Char("Agreement Title/Position")
	aggreement_bottom_date = fields.Date("Date",default=fields.Date.context_today)
	aggreement_bottom_signature = fields.Binary("Authorized Signature")
	aggreement_checkbox = fields.Boolean("I (We) provide a voided check below. I (We) understand that COMPANY is not liable for any lost monies or fees incurred for any erroneous debit entry caused by the information above if I (we) do not provide a voided check")
	
	
	#Tab 4 Customer Deal Sheet
	deal_customer_name = fields.Char("Customer Name")
	deal_customer_addr = fields.Char("Address")
	deal_customer_phone = fields.Char("Phone")
	deal_customer_fax = fields.Char("Fax")
	deal_customer_email = fields.Char("Email")
	deal_customer_contact_name = fields.Char("Customer Contact Name")
	deal_customer_ktng_rep_name = fields.Char("KT&G Rep. Name")
	deal_applied_check = fields.Char("Please check if applied?")
	deal_stamped = fields.Char("Please check if applied?")
	deal_this_list_price = fields.Char("List Price THIS")
	deal_time_list_price = fields.Char("List Price TIME")
	deal_carnival_list_price = fields.Char("List Price CARNIVAL")
	deal_this_off_invoice = fields.Char("Off Invoice THIS")
	deal_time_off_invoice = fields.Char("Off Invoice TIME")
	deal_carnival_off_invoice = fields.Char("Off Invoice CARNIVAL")
	deal_this_msa = fields.Char("MSA Refund THIS")
	deal_time_msa = fields.Char("MSA Refund TIME")
	deal_carnival_msa = fields.Char("MSA Refund CARNIVAL")
	deal_this_rebate = fields.Char("Rebate THIS")
	deal_time_rebate = fields.Char("Rebate TIME")
	deal_carnival_rebate = fields.Char("Rebate CARNIVAL")
	deal_this_invoice_net = fields.Char("Invoice net THIS")
	deal_time_invoice_net = fields.Char("Invoice net TIME")
	deal_carnival_invoice_net = fields.Char("Invoice net CARNIVAL")
	deal_special = fields.Char("Special Deals ?")
	deal_comment = fields.Char("Comments")
	signature_deal = fields.Binary("Account Manager Signature")
	deal_signature_date = fields.Date("Date",default=fields.Date.context_today)
	
	
	
	
	#Tab 5 PURCHASE ORDER
	po_company_name = fields.Char("Company Name")
	po_addr = fields.Char("Address")
	po_phone = fields.Char("Phone")
	po_fax = fields.Char("Fax")
	po_no = fields.Char("PO Number")
	signature_po_customer = fields.Binary("Customer Signature")
	po_cust_signature_date = fields.Date("Date",default=fields.Date.context_today)
	
	
	
	po_red_100_soft_qty = fields.Integer("Carnival Red 100 Soft") 
	po_blue_100_soft_qty = fields.Integer("Carnival Blue 100 Soft")
	po_silver_100_soft_qty = fields.Integer("Carnival Silver 100 Soft")
	po_menthol_100_soft_qty = fields.Integer("Carnival Menthol 100 Soft")
	po_menthol_green_100_soft_qty = fields.Integer("Carnival Menthol Green 100 Soft")    
	
	po_red_100_box_qty = fields.Integer("Carnival Red 100 Box") 
	po_blue_100_box_qty = fields.Integer("Carnival Blue 100 Box")
	po_silver_100_box_qty = fields.Integer("Carnival Silver 100 Box")
	po_menthol_100_box_qty = fields.Integer("Carnival Menthol 100 Box")
	po_menthol_green_100_box_qty = fields.Integer("Carnival Menthol Green 100 Box")    
	
	po_red_king_box_qty = fields.Integer("Carnival Red King Box") 
	po_blue_king_box_qty = fields.Integer("Carnival Blue King Box")
	po_silver_king_box_qty = fields.Integer("Carnival Silver King Box")
	po_menthol_king_box_qty = fields.Integer("Carnival Menthol King Box")
	
	po_red_100_box_qty2 = fields.Integer("Timeless Time Red 100 Box") 
	po_blue_100_box_qty2 = fields.Integer("Timeless Time Blue 100 Box")
	po_silver_100_box_qty2 = fields.Integer("Timeless Time Silver 100 Box")
	po_menthol_100_box_qty2 = fields.Integer("Timeless Time Menthol 100 Box")
	po_menthol_green_100_box_qty2 = fields.Integer("Timeless Time Menthol Green 100 Box")    
	
	po_red_king_box_qty2 = fields.Integer("Timeless Time Red King Box") 
	po_blue_king_box_qty2 = fields.Integer("Timeless Time Blue King Box")
	po_silver_king_box_qty2 = fields.Integer("Timeless Time Silver King Box")
	po_menthol_king_box_qty2 = fields.Integer("Timeless Time Menthol King Box")
	po_menthol_green_king_box_qty2 = fields.Integer("Timeless Time Menthol Green King Box")
	
	po_red_100_box_qty3 = fields.Integer("THIS Red 100 Box") 
	po_blue_100_box_qty3 = fields.Integer("THIS Blue 100 Box")
	po_silver_100_box_qty3 = fields.Integer("THIS Silver 100 Box")
	po_menthol_100_box_qty3 = fields.Integer("THIS Menthol 100 Box")
	po_menthol_green_100_box_qty3 = fields.Integer("THIS Menthol Green 100 Box")    
	
	po_red_king_box_qty3 = fields.Integer("THIS Red King Box") 
	po_blue_king_box_qty3 = fields.Integer("THIS Blue King Box")
	po_silver_king_box_qty3 = fields.Integer("THIS Silver King Box")
	po_menthol_king_box_qty3 = fields.Integer("THIS Menthol King Box")
	po_menthol_green_king_box_qty3 = fields.Integer("THIS Menthol Green King Box")
	
	
	
	
	
	
	
	
	
		