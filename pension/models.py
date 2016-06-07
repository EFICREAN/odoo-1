# -*- coding: utf-8 -*-

from openerp import models, fields, api

class res_partner2(models.Model):
	_name = "res.partner"
	_inherit = "res.partner"
	nrodoc = fields.Char(string='DNI del alumno:')
	edad   = fields.Integer(string='Edad:')
	grado = fields.Char(string='Grado:')
	seccion = fields.Char(string='Sección:')
	nombre_padre = fields.Char(string="Nombre Padre / Tutor")
	dni_padre = fields.Char(string="DNI del Padre")
	movil_padre = fields.Char(string="Movil del Padre")
	nivel_est = fields.Selection([('INICIAL','INICIAL'),('PRIMARIA','PRIMARIA'),('SECUNDARIA','SECUNDARIA')],string="Nivel estudio")
	#ids_account = fields.Many2one('account.invoice')
	
  	@api.onchange('nrodoc')
    	def _verify_valid_nrodoc(self):
    		var_nrodoc = self.nrodoc
    		if len(var_nrodoc)=0:
    	  		var_nrodoc="1"
    	  	
    		if not var_nrodoc.isdigit() or not (len(var_nrodoc)==8):
            		return {
                		'warning': {
                    		'title': "Incorrect DNI value",
                    		'message': "Es menor a 8 dígitos o no es númerico",
                		},
            		}
            		
        @api.onchange('dni_padre')
    	def _verify_valid_dnipadre(self):
    	  	var_dni_padre = self.dni_padre
    	  	if len(var_dni_padre)=0:
    	  		var_dni_padre="1"
    	  	
    		if not var_dni_padre.isdigit() or not (len(var_dni_padre)==8):
            		return {
                		'warning': {
                    		'title': "Incorrect DNI value",
                    		'message': "Es menor a 8 dígitos o no es númerico",
                		},
            		}
            	
