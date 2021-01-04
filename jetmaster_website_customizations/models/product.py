from odoo import fields, models


class ProductTemplateInherit(models.Model):
    _inherit = "product.template"
    
    
#     def _compute_product_partlist_flag(self):
#         for rec in self:
#             bom_exists = self.env['mrp.bom'].sudo().search([('product_tmpl_id', '=', rec.id)])
#             if bom_exists:
#                 rec.product_partlist_flag = True
#             else:
#                 rec.product_partlist_flag = False
# 
#     product_features = fields.Html()
#     product_brochures = fields.Binary('Brochures')
#     product_manuals = fields.Binary("Manuals")
#     brochure_name = fields.Char("Brochure Name")
#     manual_name = fields.Char("Owner's Manual Name")
#     video_link = fields.Char("Video Url")
#     product_partlist_flag = fields.Boolean('Product Partlist Flag', 
#                                            compute='_compute_product_partlist_flag',
#                                            default=False)
#     dealers_only = fields.Boolean('Dealers Only',
#                                   default=False,
#                                   help="If set, retail customers wont be able to buy main unit.")
#     
#     #OVERRIDE
#     def _is_add_to_cart_possible(self, parent_combination=None):
#         self.ensure_one()
#         res = super(ProductTemplateInherit, self)._is_add_to_cart_possible(parent_combination=parent_combination)
#         #CHECK IF THIS PRODUCT IS TO BE SOLD THROUGH DEALERS ONLY, IF YES THEN DONT ALLOW TO ADD TO CART
#         if self.dealers_only:
#             return False
#         return res
    
class ProductEnquiry(models.Model):
    _name = "product.enquiry"

#     product_id = fields.Many2one('product.template', string="Product")
#     display_name = fields.Char("Name")
#     street = fields.Char()
#     street2 = fields.Char()
#     zip = fields.Char(change_default=True)
#     city = fields.Char()
#     # state_id = fields.Many2one("res.country.state", string='State', ondelete='restrict',
#     #                            domain="[('country_id', '=?', country_id)]")
#     # country_id = fields.Many2one('res.country', string='Country', ondelete='restrict')
#     state_id = fields.Char(string='State')
#     country_id = fields.Char(string='Country')
#     email = fields.Char("Email")
#     phone = fields.Char("Phone")
#     contact_preference = fields.Selection([('phone', 'Phone'), ('email', 'Email')],
#                                           help="How do you prefer to be contacted")
#     unit_preference = fields.Selection([('new_unit', 'New Unit'), ('replace_existing', 'Replace Existing')],
#                                        help="New Unit or Replacing Existing Unit")
#     installation = fields.Selection([('required', 'Required '), ('not_required', 'Not Required')],
#                                     string="Installation")
#     house_type = fields.Selection([('single', 'Single Story '), ('double', 'Double Story')],
#                                   string="House Type")
#     unit_type = fields.Selection([('inbuilt', 'Inbuilt'), ('free_stand', 'Free Standing')])
#     unit_type_inbuilt = fields.Char("Unit Type Inbuilt")
#     unit_type_freestanding = fields.Char("Unit Type FreeStanding")
#     inbuilt_units = fields.Char("Inbuilt Unit Preference")
