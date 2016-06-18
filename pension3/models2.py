# -*- coding: utf-8 -*-

from openerp import models, fields, api
from openerp.exceptions import ValidationError


class res_partner1(models.Model):
    	_name = "res.partner"
    	_inherit = "res.partner"
    
    	@api.one
	@api.constrains('nrodoc')
	def _check_unique_constraint(self):
        	if len(self.search(['nrodoc', '=', self.nrodoc])) > 1:
                	raise ValidationError("DNI del Alumno existe debe ser único")
                	
                	
	
