# -*- coding: utf-8 -*-

from openerp import models, fields, api

class res_partner(models.Model):
	_name = "res.partner"
	_inherit = "res.partner"
	x_nrodoc = fields.Char(string='DNI del alumno:')
	x_edad   = fields.Integer(string='Edad:')
	x_grado1 = fields.Char(string='Grado:')
	x_seccion1 = fields.Char(string='Sección:')
	x_nombre_padre = fields.Char(string="Nombre Padre / Tutor")
	x_dni_padre = fields.Char(string="DNI del Padre")
	x_movil_padre = fields.Char(string="Movil del Padre")
	x_nivel = fields.Selection([('INICIAL','INICIAL'),('PRIMARIA','PRIMARIA'),('SECUNDARIA','SECUNDARIA')],string="Nivel estudio")
	
class account_invoice2(models.Model):
	_name = "account.invoice"
	_inherit = "account.invoice"
	x_dni_p = fields.Char(related='partner_id.x_dni_padre',store=True,string="Dni padre:")
	

#
	
