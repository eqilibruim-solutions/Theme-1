import json
import logging
import base64
import re
from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale
_logger = logging.getLogger(__name__)


class Custom_Website(http.Controller):

    @http.route(['/product_enquiry/product/<model("product.template"):product>'],
                type="http", auth="public", website=True)
    def product_enquiry(self, product, **kwargs):
        values = {'product': product}
        return request.render("jetmaster_website_customizations.product_enquiry_view_template", values)

    @http.route(['/save/product_enquiry'],
                type="http", auth="public", methods=['POST'], website=True, csrf=False)
    def save_product_enquiry(self, **kw):
        # print("\n\nKW:::::::::::::::::;", kw)
        enquiry_dict = {}
        Product_Enquiry = request.env['product.enquiry']

        if 'product' in kw:
            enquiry_dict['product_id'] = kw['product']

        if kw['first_name'] and kw['last_name']:
            name = kw['first_name'] + " " + kw['last_name']
            enquiry_dict['display_name'] = name

        if kw['street'] and kw['street2'] and kw['zip_code'] and kw['state'] and kw['city'] and kw['phone'] and kw[
            'email']:
            enquiry_dict['street'] = kw['street']
            enquiry_dict['street2'] = kw['street2']
            enquiry_dict['zip'] = kw['zip_code']
            enquiry_dict['city'] = kw['city']
            enquiry_dict['state_id'] = kw['state']
            enquiry_dict['phone'] = kw['phone']
            enquiry_dict['email'] = kw['email']

        if 'prefer-contacted' in kw:
            if kw['prefer-contacted'] == 'phone':
                enquiry_dict['contact_preference'] = 'phone'
            else:
                enquiry_dict['contact_preference'] = 'email'

        if 'replace-unit' in kw:
            if kw['replace-unit'] == 'new':
                enquiry_dict['unit_preference'] = 'new_unit'
            else:
                enquiry_dict['unit_preference'] = 'replace_existing'

        if 'installation' in kw:
            if kw['installation'] == 'required':
                enquiry_dict['installation'] = 'required'
            else:
                enquiry_dict['installation'] = 'not_required'

        if 'house-type' in kw:
            if kw['house-type'] == 'single':
                enquiry_dict['house_type'] = 'single'
            else:
                enquiry_dict['house_type'] = 'double'

        if 'unit-type' in kw:
            if kw['unit-type'] == 'inbuilt_type':
                enquiry_dict['unit_type'] = 'inbuilt'
            else:
                enquiry_dict['unit_type'] = 'free_stand'

        if 'unit_type_inbuilt' in kw:
            enquiry_dict['unit_type_inbuilt'] = kw['unit_type_inbuilt']

        if 'inbuilt_units_sub' in kw:
            enquiry_dict['inbuilt_units'] = kw['inbuilt_units_sub']

        if 'free_standing_units' in kw:
            enquiry_dict['unit_type_freestanding'] = kw['free_standing_units']

        # print("ENQUIRY DICT:::::::::::;",enquiry_dict)
        res = Product_Enquiry.create(enquiry_dict)
        # print("RES::::::::::::;",res)

        return request.render("jetmaster_website_customizations.product_enquiry_thanks")

    # @http.route(['/book-a-service'], type="http", auth="public", website=True, csrf=False)
    # def book_a_service_page(self, **kw):
    #     product_cat = request.env['product.public.category'].sudo().search([])
    #     products = request.env['product.product'].sudo().search([])
    #     values = {}
    #     values['categories'] = product_cat
    #     values['products'] = products
    #     return request.render("jetmaster_website_customizations.book_a_service_view_template", values)
    #
    # @http.route(['/get_products_by_category'], type="http", auth="public", website=True)
    # def get_products_by_category(self, **kw):
    #     print("HELOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
    #     if kw.get('category'):
    #         products = request.env['product.product'].sudo().search([('public_categ_ids','in',[kw.get('category')])])
    #         values = {}
    #         values['products'] = products
    #         json.dumps(values)

    @http.route(['/booking-a-service'],
                type="http", auth="public", methods=['POST'], website=True, csrf=False)
    def save_booking_service(self, **kw):
        # print("\n\nKW:::::::::::::::::;", kw)
        try:
            booking_service = {}
            if 'service_type' in kw:
                booking_service['service_type'] = kw['service_type']

            if 'service_required' in kw:
                booking_service['brand_fireplace'] = kw['service_required']

            if 'fireplace_model' in kw:
                booking_service['model_no'] = kw['fireplace_model']

            if 'serial_no' in kw:
                booking_service['serial_no'] = kw['serial_no']

            if 'promo-code' in kw:
                booking_service['promo_code'] = kw['promo-code']

            if 'first_name' in kw:
                booking_service['first_name'] = kw['first_name']

            if 'last_name' in kw:
                booking_service['last_name'] = kw['last_name']

            if 'address' in kw:
                booking_service['address'] = kw['address']

            if 'Suburb' in kw:
                booking_service['suburb'] = kw['Suburb']

            if 'contact-number' in kw:
                booking_service['phone'] = kw['contact-number']

            if 'email' in kw:
                booking_service['email'] = kw['email']

            if 'secondary-name' in kw:
                booking_service['contact_name'] = kw['secondary-name']

            if 'secondary-number' in kw:
                booking_service['phone2'] = kw['secondary-number']

            if 'desc_problem' in kw:
                booking_service['description'] = kw['desc_problem']

            if 'system_type' in kw:
                booking_service['system_type'] = kw['system_type']

            if 'fireplace-purchased-from' in kw:
                booking_service['fireplace_purchased_from'] = kw['fireplace-purchased-from']

            # print("BOOKING SERVICE DICT:::::::::::;", booking_service)
            res = request.env['booking.service'].sudo().create(booking_service)
            if res:
                return request.render("jetmaster_website_customizations.booking_service_thanks_message")

        except Exception:
            _logger.error('Exception Occurred :', e)
            return request.redirect('/book-a-service')

    @http.route(['/thank-you'],
                type="http", auth="public", methods=['POST'], website=True, csrf=False)
    def save_contact_details(self, **kw):
        # print("\n\nKW:::::::::::::::::;", kw)
        try:
            contact_details = {}
            if 'existing_fireplace' in kw:
                contact_details['existing_fireplace'] = kw['existing_fireplace']

            if 'main_reason' in kw:
                contact_details['main_reason'] = kw['main_reason']

            if 'fireplace_type' in kw:
                contact_details['fireplace_type'] = kw['fireplace_type']

            if 'about_us' in kw:
                contact_details['about_us'] = kw['about_us']

            if 'contact_name' in kw:
                contact_details['name'] = kw['contact_name']

            if 'email' in kw:
                contact_details['email'] = kw['email']

            if 'phone' in kw:
                contact_details['phone'] = kw['phone']

            if 'postcode' in kw:
                contact_details['postcode'] = kw['postcode']

            if 'comments' in kw:
                contact_details['comments'] = kw['comments']

            # print("CONTACT DETAILS DICT:::::::::::;", contact_details)
            res = request.env['contact.details'].sudo().create(contact_details)
            if res:
                return request.render("jetmaster_website_customizations.contact_us_thanks_message")

        except Exception:
            _logger.error('Exception Occurred :', e)
            return request.redirect('/contact-us')

    @http.route(['/thankyou-gallery'],
                type="http", auth="public", methods=['POST'], website=True, csrf=False)
    def save_gallery_queries(self, **kw):
        # print("\n\nKW:::::::::::::::::;", kw)
        try:
            gallery_dict = {}

            if 'gallery_product_id' in kw:
                gallery_dict['gallery_product_id'] = kw['gallery_product_id']

            if 'name' in kw:
                gallery_dict['name'] = kw['name']

            if 'email' in kw:
                gallery_dict['email'] = kw['email']

            if 'phone' in kw:
                gallery_dict['phone'] = kw['phone']

            if 'gallery-message' in kw:
                gallery_dict['message'] = kw['gallery-message']

            # print("GALLERY DICT:::::::::::;", gallery_dict)
            res = request.env['gallery.view.queries'].sudo().create(gallery_dict)
            # print("RES::::::::::::;", res)
            if res:
                return request.render("jetmaster_website_customizations.gallery_page_thanks")

        except Exception:
            _logger.error('Exception Occurred :', e)
            return request.redirect('/gallery')

    @http.route(['/gallery'], type="http", auth="public", website=True)
    def gallery_page(self, **kwargs):
        gallery_images = [x for x in request.env['gallery.view'].search([('active', '=', True)])]
        return request.render("jetmaster_website_customizations.gallery_view_template",
                              {'gallery_images': gallery_images})

    @http.route(['/dealers'], type="http", auth="public", website=True, csrf=False)
    def dealers_page(self, **kwargs):
        api_key = http.request.env['ir.config_parameter'].sudo().search([('key', '=', 'google.api_key_geocode')])
        if len(api_key) == 1:
            maps_url = "//maps.google.com/maps/api/js?key=" + api_key.value + "&callback=initialize&libraries=geometry,places"
        else:
            maps_url = "//maps.google.com/maps/api/js?key=&libraries=geometry,places"

        return request.render('jetmaster_website_customizations.dealers_view_template',
                              {'maps_script_url': maps_url,
                               })

    def create_partner_dict(self, partner):
        partners_dict = {}
        if partner.partner_latitude and partner.partner_longitude:
            if partner.street and partner.street2:
                street = partner.street + ' ' + partner.street2
            elif partner.street:
                street = partner.street
            else:
                street = partner.street2

            partners_dict['lat'] = partner.partner_latitude
            partners_dict['lng'] = partner.partner_longitude
            partners_dict['id'] = partner.id
            partners_dict['address'] = partner.contact_address
            partners_dict['street'] = street
            partners_dict['phone'] = partner.phone
            partners_dict['city'] = partner.city
            partners_dict['zip'] = partner.zip
            partners_dict['state'] = partner.state_id.name
            partners_dict['country'] = partner.country_id.name
            partners_dict['name'] = partner.name
        return partners_dict

    @http.route(['/get_all_dealers_location'], type="http", auth="public", website=True, csrf=False)
    def get_all_dealers_locations(self, **kw):
        # print("kkkkkkkkkkkkkk", kw)
        partners = []

        if kw.get('result_search'):
            limit = int(kw.get('result_search'))
        else:
            limit = 25

        res_partner = http.request.env['res.partner'].sudo().search(
            [('is_dealer', '=', True)])

        for partner in res_partner:
            if kw.get('address'):
                if re.split(',| ', kw.get('address'))[0].lower() in partner.contact_address.lower():
                    partner_obj = self.create_partner_dict(partner)
                    if partner_obj and partner_obj not in partners:
                        partners.append(partner_obj)
            else:
                partner_obj = self.create_partner_dict(partner)
                if partner_obj and partner_obj not in partners:
                    partners.append(partner_obj)

        if len(partners) != 0:
            return json.dumps({'partners': partners[:limit]})
        else:
            return json.dumps({'partners': partners})

    @http.route(['/brochures-specifications'], type="http", auth="public", website=True)
    def brochure_specification_page(self, **kwargs):
        # print("IN PRODUCT BROCHURE CONTROLLER")
        values = {}
        prod_cat_lst_b = []  # brochures list
        prod_cat_lst_m = []  # manuals list
        product_category = request.env['product.public.category'].search([])
        # productss = request.env['product.template'].search(
        #     [('product_brochures', '!=', False), ('product_manuals', '!=', False)])

        for cat_id in product_category.parents_and_self:
            if cat_id.product_tmpl_ids:
                brochures = []
                manuals = []
                for prod in cat_id.product_tmpl_ids:
                    if prod.product_brochures:
                        # print("\nproduct_tmpl_ids", prod, cat_id)
                        if prod not in brochures:
                            brochures.append(prod)
                        if cat_id.parent_id:
                            find_b = next((item for item in prod_cat_lst_b if item["category"] == cat_id.parent_id),
                                          False)
                            if find_b:
                                find_b['product'].append(prod)
                            else:
                                prod_cat_lst_b.append({'category': cat_id.parent_id, 'product': brochures})
                            # prod_cat_lst_b.append({'category': cat_id, 'product': brochures})
                        else:
                            prod_cat_lst_b.append({'category': cat_id, 'product': brochures})

                    if prod.product_manuals:
                        if prod not in manuals:
                            manuals.append(prod)
                        if cat_id.parent_id:
                            find_m = next((item for item in prod_cat_lst_m if item["category"] == cat_id.parent_id),
                                          False)
                            if find_m:
                                find_m['product'].append(prod)
                            else:
                                prod_cat_lst_m.append({'category': cat_id.parent_id, 'product': manuals})
                            # prod_cat_lst_m.append({'category': cat_id, 'product': manuals})
                        else:
                            prod_cat_lst_m.append({'category': cat_id, 'product': manuals})

        # print ("Original", prod_cat_lst_b, prod_cat_lst_m)

        res_list_b = [i for n, i in enumerate(prod_cat_lst_b) if
                      i not in prod_cat_lst_b[n + 1:]]  # remove duplicate dict from brochures list
        res_list_m = [i for n, i in enumerate(prod_cat_lst_m) if
                      i not in prod_cat_lst_m[n + 1:]]  # remove duplicate dict from manuals list
        # print("\n\nAFTER REMOVING DUPLICATES::::::::", res_list_b, res_list_m)
        values['prod_cat_lst_b'] = res_list_b
        values['prod_cat_lst_m'] = res_list_m
        return request.render("jetmaster_website_customizations.brochures_specifications_view_template", values)

    @http.route('/add_all_selected_items_to_cart', type='http', auth="public", csrf=False, website=True)
    def add_all_selected_items_to_cart(self, **post):
        try:
            # print("POST:::::::::::::::::::::;",post)
            cart_lst = json.loads(post.get('cart_lst'))
            sale_order = request.website.sale_get_order(force_create=True)
            for j in cart_lst:
                sale_order._cart_update(
                    product_id=int(j.get('product_id')),
                    add_qty=j.get('add_qty')
                )
            return json.dumps({})
        except Exception:
            return json.dumps({})
        
# class PartlistController(http.Controller):
#     
#     @http.route('/get_partlist_data', auth='user')
#     def get_partlist_data(self, **kwargs):
#         '''
#             This controller will fetch partlist data
#         '''
#         data_lst = []
#         exploded_view = False
#         if kwargs.get('product_id'):
#             bom_id = request.env['mrp.bom'].sudo().search([('product_tmpl_id', '=', int(kwargs.get('product_id')))],
#                                                           limit = 1)
#             if bom_id:
#                 count = 1
#                 for index, bom_line in enumerate(bom_id.bom_line_ids):
#                     data_dict = {}
#                     data_dict['product_id'] = bom_line.product_id.id
#                     data_dict['item_no'] = bom_line.ref_no or '-'
#                     data_dict['item_title'] = bom_line.product_id.name
#                     data_dict['item_comment'] = bom_line.comment or ''
#                     data_dict['item_description'] = bom_line.product_id.description_sale or '-'
#                     data_dict['item_partno'] = bom_line.product_id.default_code or '-'
#                     data_dict['child_bom_id'] = bom_line.child_bom_id.id if bom_line.child_bom_id else False
#                     count += 1
#                     data_lst.append(data_dict)
#                 if bom_id.exploded_view:
#                     exploded_view = bom_id.exploded_view.decode('utf-8')
#         return json.dumps({'data':data_lst, 'exploded_view':str(exploded_view)})
#     
#     @http.route('/update_partlist_in_cart', auth='public', csrf=False, website=True)
#     def update_partlist_in_cart(self, product_id, add_qty=1, set_qty=0, **kw):
#         '''
#             This is controller which update partlist
#         '''
#         sale_order = request.website.sale_get_order(force_create=True)
#         if sale_order:
#             sale_order._cart_update(
#                 product_id=int(product_id),
#                 add_qty=add_qty,
#                 set_qty=set_qty,
#                 )
#         return request.redirect(request.httprequest.referrer)
# 
# class WebsiteSaleInherit(WebsiteSale):
# 
#     @http.route(['/shop/cart/update'], type='http', auth="public", methods=['GET', 'POST'], website=True,
#                 csrf=False)
#     def cart_update(self, product_id, add_qty=1, set_qty=0, **kw):
#         # print("IN INHERITED CART UPDATE:::::::::::")
#         res = super(WebsiteSaleInherit, self).cart_update(product_id, add_qty, set_qty, **kw)
#         return request.redirect("/shop")
