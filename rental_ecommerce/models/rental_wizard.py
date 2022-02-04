# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, _


class RentalWizard(models.TransientModel):
    _inherit = 'rental.wizard'

    additional = fields.Char("Additional Comments")

    @api.depends('pricing_id', 'pickup_date', 'return_date')
    def _compute_duration(self):
        rec = super(RentalWizard, self)._compute_duration()
        for wizard in self:
            wizard.additional = wizard.rental_order_line_id.additional

