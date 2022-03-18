# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError

class ResConfigSettings(models.TransientModel):
	_inherit = 'res.config.settings'

	is_sign_invoice = fields.Boolean(String="Allow Digital Signature in Customer Invoice")
	is_sign_bill = fields.Boolean(String="Allow Digital Signature in Vendor Bill")
	is_confirm_sign_invoice = fields.Boolean(string="Required Signature on Validate Customer Invoice", default=False)
	is_confirm_sign_bill = fields.Boolean(string="Required Signature on Validate Vendor Bill",default=False)

	@api.model
	def get_values(self):
		res = super(ResConfigSettings, self).get_values()
		res.update(
			is_sign_invoice=(self.env['ir.config_parameter'].sudo().get_param('digital_signature.is_sign_invoice')),
			is_sign_bill=(self.env['ir.config_parameter'].sudo().get_param('digital_signature.is_sign_bill')),
			is_confirm_sign_invoice=(self.env['ir.config_parameter'].sudo().get_param('digital_signature.is_confirm_sign_invoice')),
			is_confirm_sign_bill=(self.env['ir.config_parameter'].sudo().get_param('digital_signature.is_confirm_sign_bill')),
		)
		return res

	def set_values(self):
		super(ResConfigSettings, self).set_values()
		self.env['ir.config_parameter'].sudo().set_param('digital_signature.is_sign_invoice',self.is_sign_invoice),
		self.env['ir.config_parameter'].sudo().set_param('digital_signature.is_sign_bill',self.is_sign_bill),
		self.env['ir.config_parameter'].sudo().set_param('digital_signature.is_confirm_sign_invoice',self.is_confirm_sign_invoice),
		self.env['ir.config_parameter'].sudo().set_param('digital_signature.is_confirm_sign_bill',self.is_confirm_sign_bill),


class AccountMove(models.Model):
	_inherit = "account.move"

	def _digital_sign_customer_invoice(self):
		is_sign_invoice = (self.env['ir.config_parameter'].sudo().get_param('digital_signature.is_sign_invoice'))
		return is_sign_invoice

	def _digital_sign_vendor_bill(self):
		is_sign_bill = (self.env['ir.config_parameter'].sudo().get_param('digital_signature.is_sign_bill'))
		return is_sign_bill

	def _confirm_sign_invoice(self):
		is_confirm_sign_invoice = (self.env['ir.config_parameter'].sudo().get_param('digital_signature.is_confirm_sign_invoice'))
		return is_confirm_sign_invoice

	def _confirm_sign_bill(self):
		is_confirm_sign_bill = (self.env['ir.config_parameter'].sudo().get_param('digital_signature.is_confirm_sign_bill'))
		return is_confirm_sign_bill
	
	def action_post(self):
		res = super(AccountMove,self).action_post()
		if self.move_type == 'out_invoice':
			if self.confirmation_digital_sign_customer_invoice_compute:
				if self.digital_signature:
					return res
				else:
					raise UserError(_('Please add Digital Signature for validate customer invoice...!'))
			else:
				return res
		elif self.move_type == 'in_invoice':
			if self.confirm_sign_bill_compute:
				if self.digital_signature:
					return res
				else:
					raise UserError(_('Please add Digital Signature for validate vendor bill...!'))
			else:
				return res
		else:
			return res

	digital_signature = fields.Binary(string="Digital Signature")
	sign_invoice_compute = fields.Text(default=_digital_sign_customer_invoice)
	digital_sign_vendor_bill_compute = fields.Text(default=_digital_sign_vendor_bill)
	confirmation_digital_sign_customer_invoice_compute = fields.Text(default=_confirm_sign_invoice)
	confirm_sign_bill_compute = fields.Text(default=_confirm_sign_bill)