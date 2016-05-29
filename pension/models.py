# -*- coding: utf-8 -*-

from openerp import models, fields, api
from openerp.osv import osv

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
	#ids_account = fields.Many2one('account.invoice')
	
class custom_account(osv.osv):
    _inherits = 'account.invoice'
    
x_dni2 = fields.Char(string="Dni padre")
def onchange_partner_id2(self, partner_id):
	if partner_id:
            p = self.env['res.partner'].browse(partner_id)
            self.x_dni2 = p.x_dni_padre
            
