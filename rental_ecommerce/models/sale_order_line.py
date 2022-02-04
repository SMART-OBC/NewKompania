# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, _


class RentalWizard(models.Model):
    _inherit = 'sale.order.line'

    additional = fields.Char("Additional Comments")

