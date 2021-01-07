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


class mail_followers(models.Model):
	_inherit = "mail.followers"
	
	@api.model
	def create(self, vals):
		
		try:
			return super(mail_followers, self).create(vals)
		except Exception as e:
			self._cr.rollback()
			self._cr.execute("delete from mail_followers where res_model='%s' and partner_id='%s' and res_id='%s' " % (vals['res_model'], vals['partner_id'], vals['res_id']) )
			
			is_exist = self.env['mail.followers'].sudo().search([
															('res_model', '=', vals['res_model']), 
															('partner_id', '=', vals['partner_id']), 
															('res_id', '=', vals['res_id']),
															])
															
			
			return is_exist
															
		
