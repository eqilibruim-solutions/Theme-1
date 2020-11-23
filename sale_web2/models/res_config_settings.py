# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from ast import literal_eval

from odoo import api, models, fields


class website(models.Model):
    _inherit = 'website'



    sync_url = fields.Char( string="Server URL")
    sync_user = fields.Char( string="User")
    sync_pwd = fields.Char( string="Password")
    sync_db = fields.Char( string="Database")
    sync_port = fields.Char( string="Port")
    
    

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'



    sync_url = fields.Char(related="website_id.sync_url", readonly=False, string="Server URL", config_parameter="sync_url")
    sync_user = fields.Char(related="website_id.sync_user", readonly=False, string="User", config_parameter="sync_user")
    sync_pwd = fields.Char(related="website_id.sync_pwd", readonly=False, string="Password", config_parameter="sync_pwd")
    sync_db = fields.Char(related="website_id.sync_db", readonly=False, string="Database", config_parameter="sync_db")
    sync_port = fields.Char(related="website_id.sync_port", readonly=False, string="Port", config_parameter="sync_port")
    
