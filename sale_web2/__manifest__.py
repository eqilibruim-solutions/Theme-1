# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Order Synch Server',
    'version': '13.1.5.1',
    'category': 'Website',
    'depends': ['website_sale', 'mail'],
    'description': """
    Quick Product add into Cart
    
    """,
    'data': [
    	'views/sale_views.xml',
        'security/ir.model.access.csv',
    ],
    'summary':'Quick Product add into Cart and other modifications in website order processing',
    'demo': [
    ],
    'author': 'KPAK',
	'qweb': [ ],
    'installable': True,
    'auto_install': False,
}
