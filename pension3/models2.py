# -*- coding: utf-8 -*-

from openerp import models, fields, api
from openerp.exceptions import ValidationError


class res_partner1(models.Model):
    	_name = "res.partner"
    	_inherit = "res.partner"
    
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
                	
                	
	
