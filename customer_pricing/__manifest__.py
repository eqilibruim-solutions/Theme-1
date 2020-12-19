# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Customer Based Pricelist',
    'version': '13.1.5.1',
    'category': 'Website',
    'depends': ['product'],
    'description': """
    Clarico Theme Extension
    """,
    'data': [
        'views/templates.xml',
        'views/product_views.xml',
        'security/ir.model.access.csv',
        'security/website_sale.xml',
    ],
    'summary':'Customer Based Pricelist',
    'demo': [
    ],
    'author': '',
	'qweb': [ ],
    'installable': True,
    'auto_install': False,
}
