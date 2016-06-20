# -*- coding: utf-8 -*-

from openerp import models, fields, api
from openerp.exceptions import ValidationError

class res_partner2(models.Model):
	_name = "res.partner"
	_inherit = "res.partner"
	nrodoc = fields.Char(string='DNI del alumno:', required=True)
	edad   = fields.Integer(string='Edad:', required=True)
	grado = fields.Char(string='Grado:',required=True)
	seccion = fields.Char(string='Sección:',required=True)
	nombre_padre = fields.Char(string="Nombre Padre / Tutor",required=True)
	dni_padre = fields.Char(string="DNI del Padre",required=True)
	movil_padre = fields.Char(string="Movil del Padre")
	nivel_est = fields.Selection([('INICIAL','INICIAL'),('PRIMARIA','PRIMARIA'),('SECUNDARIA','SECUNDARIA')],required=True,string="Nivel estudio")
	mobile = fields.Char(string="movil",related="movil_padre")
	#ids_account = fields.Many2one('account.invoice')
	
