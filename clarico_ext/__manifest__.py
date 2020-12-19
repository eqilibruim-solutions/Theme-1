# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Clarico Theme Extension',
    'version': '13.1.5.1',
    'category': 'Website',
    'depends': ['theme_clarico_vega'],
    'description': """
    Clarico Theme Extension
    """,
    'data': [
        'views/templates.xml',
        'views/product_views.xml',
        'security/ir.model.access.csv',
        'security/website_sale.xml',
    ],
    'summary':'Clarico Theme Extension',
    'demo': [
    ],
    'author': 'KPAK',
	'qweb': [ ],
    'installable': True,
    'auto_install': False,
}
