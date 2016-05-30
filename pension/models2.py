# -*- coding: utf-8 -*-

from openerp import models, fields, api


class custom_account(models.Model):
    	_name = "account.invoice"
    	_inherit = "account.invoice"
    
	x_dni2 = fields.Char(string="Dni padre")

	@api.onchange("partner_id")
	def _onchange_partner_id2(self):
		p = self.env['res.partner'].search([('partner_id', '=', partner_id)])
		for pp in p:
			if pp['x_dni_padre']:
				self.x_dni2 = pp['x_dni_padre']
				print('dni padre : %s',self.x_dni2)
