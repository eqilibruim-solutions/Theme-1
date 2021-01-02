# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Clarico Theme Extension',
    'version': '13.1.5.1',
    'category': 'Website',
    'depends': ['website_sale', 'jetmaster_website_customizations'],
    'description': """
    Clarico Theme Extension
    """,
    'data': [
        'views/templates.xml',
        'views/enroll.xml',
        'views/product_views.xml',
        'security/ir.model.access.csv',
        'security/website_sale.xml',
    ],
    
	'qweb': [
			'static/src/xml/templates.xml',
			],
	
    'summary':'Clarico Theme Extension',
    'demo': [
    ],
    'author': 'KPAK',
    'installable': True,
    'auto_install': False,
}
