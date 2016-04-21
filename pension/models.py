# -*- coding: utf-8 -*-

from openerp import models, fields, api

class res_partner(models.Model):
	_name = "res.partner"
	_inherit = "res.partner"
	x_nrodoc = fields.Char(string='DNI del alumno:')
	x_edad   = fields.Integer(string='Edad:')
	x_grado = fields.Char(string='Grando:')
	x_seccion = fields.Char(string='SeccióOD:')
	x_nombre_padre = fields.Char(string="Nombre Padre / Tutor")
	x_dni_padre = fields.Char(string="DNI del Padre")
	x_movil_padre = fields.Char(string="Movil del Padre")
#
	
