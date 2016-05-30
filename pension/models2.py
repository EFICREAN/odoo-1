# -*- coding: utf-8 -*-

from openerp import models, fields, api


class custom_account(models.Model):
    	_name = "account.invoice"
    	_inherit = "account.invoice"
    
	x_dni2 = fields.Char(string="Dni padre")

	@api.multi
	def onchange_partner_id2(self, partner_id):
		if partner_id:
            		p = self.env['res.partner'].browse(partner_id)
            		self.x_dni2 = p.x_dni_padre
