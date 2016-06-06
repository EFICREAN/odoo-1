# -*- coding: utf-8 -*-

from openerp import models, fields, api

class res_partner2(models.Model):
	_name = "res.partner"
	_inherit = "res.partner"
	nrodoc = fields.Integer(string='DNI del alumno:')
	edad   = fields.Integer(string='Edad:')
	grado = fields.Char(string='Grado:')
	seccion = fields.Char(string='Sección:')
	nombre_padre = fields.Char(string="Nombre Padre / Tutor")
	dni_padre = fields.Integer(string="DNI del Padre")
	movil_padre = fields.Char(string="Movil del Padre")
	nivel_est = fields.Selection([('INICIAL','INICIAL'),('PRIMARIA','PRIMARIA'),('SECUNDARIA','SECUNDARIA')],string="Nivel estudio")
	#ids_account = fields.Many2one('account.invoice')
	

            
