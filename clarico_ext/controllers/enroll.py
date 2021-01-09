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
from time import sleep

	
	
	   


	   	
	
class EmiproThemeBase(http.Controller):
	
	@http.route(['/page/enroll_me'], auth='public',
				type='http', website=True, methods=['POST', 'GET'], csrf=False)
	def enroll_me(self, **kwargs):
		print (1)
		
		value = {}
		
		return request.render(
			'clarico_ext.enroll_me_form', value
		)
		
		
		
	@http.route(['/page/enrolled'], auth='public',
				type='http', website=True, methods=['POST', 'GET'], csrf=False)
	def enrolled(self, **kwargs):
		return request.render(
			'clarico_ext.enroll_done', {}
		)
		
		
	def write_image(self):
		try:
			record = request.env['enroll.partner'].sudo().browse(request.session['id'])
			print (request.session['vals'].keys(), '\nKKKKKKKKKKKKKKKKKKKKKK')
			record.write(request.session['vals'])
		except:
			print ('IN EXCEPTIONNNNNNNNNNNNNNNNNNNN')
			request._cr.rollback()
			import traceback
			trace = traceback.format_exc()
			print (trace, "\n\n\n TRACEEEEEEEEEEEEEEEEEEEEEE")
			if 'could not serialize access due to concurrent' in trace:
				sleep(0.50)
				write_image()
				
		return 1
		
		
	@http.route(['/page/submit_enroll_images'], auth="public", type='json', csrf=False)
	def submit_enroll_images(self, **kw):
		values = {
				kw['field']: kw['bin_data'][22:].encode('utf-8'),
				}
		if kw['done'] == 'no':
			request.session['id'] = kw['id']
			if 'vals' not in request.session:
				request.session['vals'] = values
			else:
				request.session['vals'].update(values) 
				
				
		else:
			request.session['vals'].update(values) 
			ret = self.write_image()
		
		
		
	
	@http.route(['/page/submit_enroll_action'], auth="public", type='json', csrf=False)
	def submit_enroll_action(self, **kw):
		print ("In method--------------------\n\n")
		print (kw)
		
		kw = kw['data']
		values = {}
		
		for item in kw:
			if item['value']:
				values[item['name']] = item['value']
				if item['name'] == 'aggreement_checkbox' and item['value'] == 'on':  
					values[item['name']] = True
				if item['name'] == 'aggreement_checkbox' and item['value'] != 'on':  
					values[item['name']] = False
					
		
		id = request.env['enroll.partner'].sudo().create(values)
		
		return json.dumps({'created': id.id})
		
		
# 	@http.route(['/page/submit_enroll_action'], type='json', auth="public", methods=['GET', 'POST'], website=True, csrf=False)
# 	def submit_enroll_action(self, **kwargs):
# 		print ('In method---------------------------------------\n\n')
# 		print (kwargs)
		
		
		
		
	
	
	
	
		   
		   
		   
		   
		   
		   
		   
		   
		   
	
	
	
