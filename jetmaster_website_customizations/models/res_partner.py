from odoo import fields, models, api


class ResPartnerInherit(models.Model):
    _inherit = "res.partner"

    is_dealer = fields.Boolean("Is A Dealer", default=False)
