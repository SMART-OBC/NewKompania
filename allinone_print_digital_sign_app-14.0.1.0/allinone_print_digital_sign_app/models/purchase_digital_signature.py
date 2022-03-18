# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError

class ResConfigSettings(models.TransientModel):
	_inherit = 'res.config.settings'

	is_sign_purchase = fields.Boolean(String="Allow Digital Signature in Purchase")
	is_confirm_sign_purchase = fields.Boolean(string="Required Signature on Confirm Purchase Order",default=False)

	@api.model
	def get_values(self):
		res = super(ResConfigSettings, self).get_values()
		res.update(
			is_sign_purchase=(self.env['ir.config_parameter'].sudo().get_param('digital_signature.is_sign_purchase')),
			is_confirm_sign_purchase=(self.env['ir.config_parameter'].sudo().get_param('digital_signature.is_confirm_sign_purchase'))
		)
		return res

	def set_values(self):
		super(ResConfigSettings, self).set_values()
		self.env['ir.config_parameter'].sudo().set_param('digital_signature.is_sign_purchase',self.is_sign_purchase),
		self.env['ir.config_parameter'].sudo().set_param('digital_signature.is_confirm_sign_purchase',self.is_confirm_sign_purchase),


class PurchaseOrder(models.Model):
	_inherit = "purchase.order"

	@api.model
	def _digital_sign_purchase(self):
		is_sign_purchase = (self.env['ir.config_parameter'].sudo().get_param('digital_signature.is_sign_purchase'))
		return is_sign_purchase

	@api.model
	def _confirm_sign_purchase(self):
		is_confirm_sign_purchase = (self.env['ir.config_parameter'].sudo().get_param('digital_signature.is_confirm_sign_purchase'))
		return is_confirm_sign_purchase

	def button_confirm(self):
		res = super(PurchaseOrder,self).button_confirm()
		if self.confirm_sign_purchase_compute:
			if self.digital_signature:
				return res
			else:
				raise UserError(_('Please add Digital Signature for confirm purchase order...!'))
		else:
			return res
		return res

	digital_signature = fields.Binary(string="Digital Signature")
	digital_sign_purchase_compute = fields.Text(default=_digital_sign_purchase)
	confirm_sign_purchase_compute = fields.Text(default=_confirm_sign_purchase)
