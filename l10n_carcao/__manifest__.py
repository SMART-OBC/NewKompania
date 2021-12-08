# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

#    Module programed and financed by:
#    Vauxoo, C.A. (<http://vauxoo.com>).
#    Our Community team mantain this module:
#    https://launchpad.net/~openerp-venezuela

{
    'name' : 'Curacao - Accounting',
    'author': ['SMART'],
    'category': 'Accounting/Localizations/Account Charts ',
    'description':
"""
Chart of Account for Curacao.
===============================


""",
    'depends': ['account',
    ],
    'data': [
             'data/l10n_ve_chart_data.xml',
             'data/account.account.template.csv',
             'data/l10n_ve_chart_post_data.xml',
             # 'data/account_data.xml',
             # 'data/account_tax_data.xml',
             # 'data/account_chart_template_data.xml'
    ],
    'demo': [
        'demo/demo_company.xml',
    ],
}
