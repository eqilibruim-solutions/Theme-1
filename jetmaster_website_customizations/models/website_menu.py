from odoo import models, api
# from odoo.exceptions import UserError


class WebsiteMenuInherit(models.Model):
    _inherit = "website.menu"

    @api.model
    def create(self, vals):
        website_urls = ["/", "/shop", '/gallery', '/book-a-service', '/contact-us']
        if "website_id" in vals and vals.get('url') in website_urls:
            website_menu = self.env['website.menu'].search(
                [('url', '=', '/default-main-menu'), ('website_id', '=', int(vals.get('website_id')))])
            if website_menu:
                vals['parent_id'] = website_menu.id
        res = super(WebsiteMenuInherit, self).create(vals)
        return res

    # def write(self, vals):
    #     # print("IN WRITE::::::::::::::", self, vals)
    #     website_urls = ["/", "/shop", '/gallery', '/book-a-service', '/contact-us', '/direct-vent-flue-systems',
    #                     '/blog', '/brochures-specifications']
    #     website_menu = self.env['website.menu'].search(
    #         [('url', '=', '/default-main-menu'), ('website_id', '=', self.website_id.id)])
    #
    #     if "parent_id" in vals and self.website_id.id == website_menu.website_id.id and self.url in website_urls:
    #         raise UserError("You cannot change the parent for the menu {}".format(self.name))
    #     res = super(WebsiteMenuInherit, self).write(vals)
    #     return res

    def _compute_visible(self):
        res = super(WebsiteMenuInherit, self)._compute_visible()
        hide_menus = ['/', '/shop', '/blog']
        hide_menus_names = ['Home', 'Shop', 'Blog']
        hide_menus_parent = ['Resources']
        for menu in self:
            visible = True
            if menu.url in hide_menus and menu.name in hide_menus_names and menu.parent_id.name not in hide_menus_parent:
                visible = False
            menu.is_visible = visible
