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


	
	
	   


	   	
	
class EmiproThemeBase(http.Controller):
	
	@http.route(['/page/enroll_me'], auth='public',
				type='http', website=True, methods=['POST', 'GET'], csrf=False)
	def enroll_me(self, **kwargs):
		print (1)
		
		value = {}
		
		return request.render(
			'clarico_ext.show_doctors_list', value
		)
		
		
		
	
	
	
	
		   
		   
		   
		   
		   
		   
		   
		   
		   
	
	
	
