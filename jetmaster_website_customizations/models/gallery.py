from odoo import api, fields, models
from odoo.addons.http_routing.models.ir_http import slug
import logging

_logger = logging.getLogger(__name__)


class GalleryView(models.Model):
    _name = 'gallery.view'
    _description = 'Gallery View'
    _order = "id desc"

#     name = fields.Char('Name')
#     product_id = fields.Many2one('product.template', string="Product")
#     product_slug_url = fields.Char('Slug Product Url', compute="_compute_shop_product_slug", store=True)
#     gallery_image = fields.Binary('Gallery Image')
    active = fields.Boolean('Active', default=True)
# 
#     @api.depends('product_id')
#     def _compute_shop_product_slug(self):
#         for prod in self:
#             if prod.product_id:
#                 prod.product_slug_url = '/shop/product/' + slug(prod.product_id)


class GalleryViewQueries(models.Model):
    _name = "gallery.view.queries"
    _description = "Gallery View Queries"
    _order = "id desc"

#     gallery_product_id = fields.Many2one('product.template', string="Product")
#     name = fields.Char('Name', required=1)
#     email = fields.Char('Email', required=1)
#     phone = fields.Char('Phone', required=1)
#     message = fields.Text('Message')
