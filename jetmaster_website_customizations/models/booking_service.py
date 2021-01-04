from odoo import fields, models


class BookingService(models.Model):
    _name = "booking.service"
    _order = "id desc"
    _description = "Booking Service"

#     service_type = fields.Char(string="Service Type", required=1)
#     brand_fireplace = fields.Selection([('HAG', "Heat & Glow"),
#                                         ('JG', 'Jetmaster-Gas'),
#                                         ('horizon', 'Horizon')], string="Fireplace Brand",
#                                        required=1)
#     model_no = fields.Char(string="Model", required=1)
#     promo_code = fields.Char(string="Promo Code")
#     serial_no = fields.Char(string="Serial Number")
#     first_name = fields.Char(string="First Name", required=1)
#     last_name = fields.Char(string="Last Name", required=1)
#     address = fields.Text(string="Address", required=1)
#     suburb = fields.Char(string="Suburb", required=1)
#     phone = fields.Char(string="Phone", required=1)
#     email = fields.Char(string="Email", required=1)
#     contact_name = fields.Char(string="Secondary Contact Name")
#     phone2 = fields.Char(string="Secondary Contact Number")
#     fireplace_purchased_from = fields.Char(string="Fireplace Purchased From")
#     # system_type = fields.Selection([('natural_gas', 'Natural Gas'), ('LPG', 'LPG')],
#     #                                string="System Type")
#     system_type = fields.Char(string="System Type")
#     description = fields.Text(string="Problem Description")
