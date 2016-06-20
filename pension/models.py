# -*- coding: utf-8 -*-

from openerp import models, fields, api
from openerp.exceptions import ValidationError

class res_partner2(models.Model):
	_name = "res.partner"
	_inherit = "res.partner"
	nrodoc = fields.Char(string='DNI del alumno:', required=False)
	edad   = fields.Integer(string='Edad:', required=False)
	grado = fields.Char(string='Grado:',required=False)
	seccion = fields.Char(string='Sección:',required=False)
	nombre_padre = fields.Char(string="Nombre Padre / Tutor",required=False)
	dni_padre = fields.Char(string="DNI del Padre",required=False)
	movil_padre = fields.Char(string="Movil del Padre")
	nivel_est = fields.Selection([('INICIAL','INICIAL'),('PRIMARIA','PRIMARIA'),('SECUNDARIA','SECUNDARIA')],required=False,string="Nivel estudio")
	mobile = fields.Char(string="movil",related="movil_padre")
	#ids_account = fields.Many2one('account.invoice')
	
