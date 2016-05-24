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
	
	x_dni_p = fields.Char(string='Dni padre:')
	
	#comment = fields.Many2one('res.partner','Comment',compute='_compute_com')
	
	#commercial_partner_id = fields.Many2one('res.partner', string='Commercial Entity',
        #related='partner_id.commercial_partner_id', store=True, readonly=True,
        #help="The commercial entity that will be used on Journal Entries for this invoice")
	
	
