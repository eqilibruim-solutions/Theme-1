from odoo import api, fields, models
import logging


class MrpBomInherit(models.Model):
    _inherit = 'mrp.bom'
    
    exploded_view = fields.Binary('Exploded View')

class MrpBomLineInherit(models.Model):
    _inherit = 'mrp.bom.line'
    
    ref_no = fields.Char('Ref No.',
                         copy=False,
                         help="Reference Number")
    comment = fields.Text('Comment',
                          copy=False,
                          help="Comment")