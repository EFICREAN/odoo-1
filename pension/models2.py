# -*- coding: utf-8 -*-

from openerp import models, fields, api


class custom_account(models.Model):
    	_name = "account.invoice"
    	_inherit = "account.invoice"
    
	x_grado1 = fields.Char(string='Grado:')
	x_seccion1 = fields.Char(string='Sección:')
	x_nivel = fields.Selection([('INICIAL','INICIAL'),('PRIMARIA','PRIMARIA'),('SECUNDARIA','SECUNDARIA')],string="Nivel estudio")

class custom_account(models.Model):
    	_name = "account.voucher"
    	_inherit = "account.voucher"
    
	x_grado1 = fields.Char(string='Grado:')
	x_seccion1 = fields.Char(string='Sección:')
	x_nivel = fields.Selection([('INICIAL','INICIAL'),('PRIMARIA','PRIMARIA'),('SECUNDARIA','SECUNDARIA')],string="Nivel estudio")
	
	#@api.onchange("partner_id")
	#def _onchange_partner_id2(self):
	#	p = self.env['res.partner'].search([('partner_id', '=', partner_id)])
	#	for pp in p:
	#		self.x_dni2 = pp['x_dni_padre']
	#		print('dni padre : %s',self.x_dni2)
