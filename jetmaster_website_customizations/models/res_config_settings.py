from odoo import fields,models


class ResConfigSettingsInherit(models.TransientModel):
    _inherit = "res.config.settings"

    website_logo_2 = fields.Binary(related="website_id.logo2",readonly=False)


class WebsiteInherit(models.Model):
    _inherit = "website"

    logo2 = fields.Binary('Website Logo 2', help="Display this logo on the website.")
