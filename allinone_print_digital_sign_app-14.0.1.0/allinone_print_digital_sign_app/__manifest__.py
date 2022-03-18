# -*- coding: utf-8 -*-

{
    'name' : 'Odoo Digital Signature for Sales, Purchase, Invoices and Inventory',
    'author': "Edge Technologies",
    'version' : '14.0.1.0',
    'live_test_url':'https://youtu.be/J_HwVQRp7_0',
    'images':['static/description/main_screenshot.png'],
    'summary' : 'All in one Digital Signature Documents print Digital Sign on Sales Digital Sign on Purchase Digital Signature on Invoice report Digital Sign on invoice Digital Sign on Inventory Digital Sign on PDF reports print Digital Signature on sale report sign',
    'description' : """
                        This module helps to Gives Digital Signature in Sales, Purchase,
                        Invoices and Inventory, including PDF Reports,According to Given Configuration.
    """,
    'depends': ['base','sale_management','purchase','account','stock'],
    "license" : "OPL-1",
    'data': [
        'views/sale_digital_signature.xml',
        'views/purchase_digital_signature.xml',
        'views/inventory_digital_signature.xml',
        'views/invoice_digital_signature.xml',
        'reports/sale_digital_signature.xml',
        'reports/purchase_digital_signature.xml',
        'reports/inventory_digital_signature.xml',
        'reports/invoice_digital_signature.xml',
    ],
    'installable' : True,
    'auto_install' : False,
    'price': 8.00,
    'currency': 'EUR',
    'category' : 'Extra Tools',
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
