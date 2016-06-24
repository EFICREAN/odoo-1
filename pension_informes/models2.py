# -*- coding: utf-8 -*-

from openerp import models, fields, api
from openerp.exceptions import ValidationError


class res_partner1(models.Model):
    	_name = "res.partner"
    	_inherit = "res.partner"
    	
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

    	
    	@api.one
	@api.constrains('nrodoc', 'dni_padre')
	def _check_dni(self):
    		if self.nrodoc == self.dni_padre:
        		raise ValidationError("DNI alumno/padre deben ser únicos")
    	
    	_sql_constraints = [
        	('nrodoc_unique',
         	'UNIQUE(nrodoc)',
         	"DNI del alumno debe ser único"),
         	('dni_padre_unique',
         	'UNIQUE(dni_padre)',
         	"DNI del padre debe ser único"),
    	]
    	
    	#@api.one
	#@api.constrains('nrodoc')
	#def _check_unique_constraint(self):
	#	s_count = self.search_count(['nrodoc', '=', self.nrodoc])
        #	if len(self.search(['nrodoc', '=', self.nrodoc])) > 1:
         #       	raise ValidationError("DNI del Alumno existe debe ser único")
                	
                	
	
