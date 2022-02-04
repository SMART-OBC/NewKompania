# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Rental System',
    'version': '1.0.1',
    'category': 'POS ',
    'sequence': 20,
    'summary': '',
    'description': "",
    'depends': ['website','website_sale', 'sale', 'website_payment', 'website_mail', 'website_form', 'portal_rating', 'digest'],
    'data': [
        'security/base_groups.xml',
        'data/data.xml',
        'views/rental_wizard.xml',
        'views/sale_rental.xml',
        'views/templates.xml',
        'views/snippets/snippets.xml',
        'views/snippets/s_dynamic_snippet_products.xml',
        'views/snippets/s_products_searchbar.xml',

    ],
    'demo': [

    ],
    'installable': True,
    'application': True,
    'qweb': ['static/src/xml/*.xml'],
    'website': '',
}
