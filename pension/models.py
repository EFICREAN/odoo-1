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
	
	@api.one
        @api.constrains('nrodoc')
    	def _check_nrodoc(self):
    		var_nrodoc = self.nrodoc
    		if len(var_nrodoc)==0:
    	  		var_nrodoc="1"
    		if not var_nrodoc.isdigit() or not (len(var_nrodoc)==8):
            		raise ValidationError("Error ingreso DNI alumno")
            		
        @api.one
        @api.constrains('dni_padre')
    	def _check_dni_padre(self):
    	  	var_dni_padre = self.dni_padre
    	  	if len(var_dni_padre)==0:
    	  		var_dni_padre="1"
    		if not var_dni_padre.isdigit() or not (len(var_dni_padre)==8):
            		raise ValidationError("Error ingreso DNI padre")	

	@api.one
        @api.constrains('edad')
    	def _check_edad(self):
    		if self.edad==0:
            		raise ValidationError("Error Edad")
