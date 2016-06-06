# -*- coding: utf-8 -*-

from openerp import models, fields, api


class custom_account(models.Model):
    	_name = "account.invoice"
    	_inherit = "account.invoice"
    
	grado = fields.Char(string='Grado:',related="partner_id.grado")
	seccion = fields.Char(string='Sección:',related="partner_id.seccion")
	nivel_est = fields.Selection([('INICIAL','INICIAL'),('PRIMARIA','PRIMARIA'),('SECUNDARIA','SECUNDARIA')],string="Nivel estudio",related="partner_id.nivel_est")

class custom_account_v(models.Model):
    	_name = "account.voucher"
    	_inherit = "account.voucher"
    
	grado = fields.Char(string='Grado:',related="partner_id.grado")
	seccion = fields.Char(string='Sección:',related="partner_id.seccion")
	nivel_est = fields.Selection([('INICIAL','INICIAL'),('PRIMARIA','PRIMARIA'),('SECUNDARIA','SECUNDARIA')],string="Nivel estudio",related="partner_id.nivel_est")

	#@api.onchange("partner_id")
	#def _onchange_partner_id2(self):
	#	p = self.env['res.partner'].search([('partner_id', '=', partner_id)])
	#	for pp in p:
	#		self.x_dni2 = pp['x_dni_padre']
	#		print('dni padre : %s',self.x_dni2)
