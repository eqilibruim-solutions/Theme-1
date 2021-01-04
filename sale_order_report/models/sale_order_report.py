from odoo import api, models,fields
import datetime
 
class PickingTotalQty(models.Model):
    _inherit = 'sale.order'

    tot_sale_qty = fields.Float(compute='_calculate_sale_qty', string='Total Quantity', help="Total Sale quantity in active document")

    def _calculate_sale_qty(self):
        for rs in self:
            sumqty = 0
            for line in rs.order_line:
                sumqty += line.product_uom_qty
        rs.tot_sale_qty = sumqty
