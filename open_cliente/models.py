# -*- coding: utf-8 -*-

from openerp import models, fields, api

class res_partner(models.Model):
	_name = "res.partner"
	_inherit = "res.partner"
	x_tipocont = fields.Selection([('C1','C'),('C2','No grato'),('C3','P'),('C4','Comp/Trafa')], string='Tipo contacto')
	x_genero = fields.Selection([('C1','Mujer'),('C2','Hombre')], string='Tipo contacto')
  	x_rebote= fields.Selection([('R1','Hard'),('R2','Soft')], string='Rebote')
  	x_operador = fields.Selection([('o1','Movistar'),('o2','Claro'),('o3','Bitel'),('o4','Entel')],string='Operador')
  	x_tipored= fields.Selection([('R1','RPC'),('R2','RPE')], string='Rebote')
  	x_name1= fields.Char(string='Nombre 1')
  	x_name2= fields.Char(string='Nombre 2')
  	x_apellido1 = fields.Char(string='Apellido 1')
  	x_apellido2 = fields.Char(string='Apellido 2')
  	x_email2 = fields.Char(string='Email 2')
  	x_phone2 = fields.Char(string='Telefono fijo 2')
  	x_movil2 = fields.Char(string='Movil adicional 1')
  	x_movil3 = fields.Char(string='Movil adicional 2')
  	x_tipodoc = fields.Char(string='Tipo documento de dentidad')
  	x_nrodoc = fields.Char(string='Nro. de documento de identidad')
  	x_nrodpto = fields.Char(string='Nro. de documento de identidad')
  	x_refdir = fields.Text(string='Referencia dirección')
	urb_id = fields.Many2one('open_cliente.urb',string="Distritos")

class urb(models.Model):
	_name = "open_cliente.urb"
	name = fields.Char(string='Nombre Distrito')
	res_partner_id = fields.One2many('res.partner','urb_id', String="Distrito")
	

