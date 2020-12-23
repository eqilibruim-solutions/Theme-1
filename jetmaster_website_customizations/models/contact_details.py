from odoo import fields, models


class ContactDetails(models.Model):
    _name = "contact.details"
    _order = "id desc"
    _description = "Contact Details"

    existing_fireplace = fields.Selection([('yes', "Yes"),
                                           ('no', 'No')], string="Existing Fireplace",
                                          default="yes")
    main_reason = fields.Selection([('style', "Style"),
                                    ('family', 'Family'),
                                    ('heating', 'heating'),
                                    ('other', 'Other')], string="Existing Fireplace", default="style")
    fireplace_type = fields.Selection([('gas', "Gas Fireplace"),
                                       ('openwood', 'Open Wood Fireplace'),
                                       ('electric', 'Electric Fireplace'),
                                       ('other', 'OTHER')], string="Type of Fireplace",
                                      default="gas")
    about_us = fields.Selection([('search_engine', "Search Engine"),
                                 ('advertising', 'Advertising'),
                                 ('word_of_mouth', 'Word of Mouth'),
                                 ('other', 'Other')], string="Resource",
                                default="search_engine")
    name = fields.Char(string="Name", required=1)
    phone = fields.Char(string="Phone", required=1)
    email = fields.Text(string="Email", required=1)
    postcode = fields.Char(string="Postcode")
    comments = fields.Text(string="Comments")
