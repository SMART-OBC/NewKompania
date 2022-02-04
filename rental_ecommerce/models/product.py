# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, _


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    def get_href(self):
        self.website_url = self.website_url.replace('shop','rent')