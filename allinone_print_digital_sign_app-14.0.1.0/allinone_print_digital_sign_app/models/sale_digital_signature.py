# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError

class ResConfigSettings(models.TransientModel):
	_inherit = 'res.config.settings'

	is_sign_sale = fields.Boolean(String="Allow Digital Signature for Sale")
	is_confirm_sign_sale = fields.Boolean(string="Required Signature on Confirm Sale Order")

	@api.model
	def get_values(self):
		res = super(ResConfigSettings, self).get_values()
		res.update(
			is_sign_sale=(self.env['ir.config_parameter'].sudo().get_param('digital_signature.is_sign_sale')),
			is_confirm_sign_sale=(self.env['ir.config_parameter'].sudo().get_param('digital_signature.is_confirm_sign_sale'))
		)
		return res

	def set_values(self):
		super(ResConfigSettings, self).set_values()
		self.env['ir.config_parameter'].sudo().set_param('digital_signature.is_sign_sale',self.is_sign_sale),
		self.env['ir.config_parameter'].sudo().set_param('digital_signature.is_confirm_sign_sale',self.is_confirm_sign_sale),


class SaleOrder(models.Model):
	_inherit = "sale.order"

	@api.model
	def _digital_sign_sale_order(self):
		is_sign_sale = (self.env['ir.config_parameter'].sudo().get_param('digital_signature.is_sign_sale'))
		return is_sign_sale

	@api.model
	def _confirm_sign_sale(self):
		is_confirm_sign_sale = (self.env['ir.config_parameter'].sudo().get_param('digital_signature.is_confirm_sign_sale'))
		return is_confirm_sign_sale


	def action_confirm(self):
		if self.confirm_sign_sale_compute and self.digital_signature == False:
			raise UserError(_('Please add Digital Signature for confirm sale order...!'))
		res = super(SaleOrder,self).action_confirm()
		return res

	digital_signature = fields.Binary(string="Digital Signature")
	digital_sign_sale_order_compute = fields.Text(default=_digital_sign_sale_order)
	confirm_sign_sale_compute = fields.Text(default=_confirm_sign_sale)
