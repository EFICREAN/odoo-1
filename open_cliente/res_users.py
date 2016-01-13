## -*- coding: utf-8 -*-

from openerp import models, fields, api

class btr(models.Model):
        _name = "res.users"
        _inherit = "res.users"
        x_nombre1 = fields.Char(string='Primer Nombre:')
        x_nombre2 = fields.Char(string='Segundo Nombre:')
        x_apellido1 = fields.Char(string='Primer Apellido:')
        x_apellido2 = fields.Char(string='Segundo Apellido:')
        x_email1 = fields.Char(string='Correo:')
        x_email2 = fields.Char(string='Correo Alternativo:')
        x_telefono_fijo1 = fields.Char(string='Telefono fijo:')
	x_movil1 = fields.Char(string='Movil principal:')
	x_movil2 = fields.Char(string='Movil adicional:')
	x_direcc = fields.Char(string='Direccion:')
	x_dpto = fields.Char(string= 'Nro de dpto:')
	x_refdir = fields.Char(string='Referencia de direccion')
	x_dirsec = fields.Char(string='Direccion secundaria:')
	x_dni = fields.Char(string='DNI:')
	x_fechanac = fields.Date(string='Fecha de nacimiento:')
	x_edadact = fields.Integer(string='Edad actual:')
	x_estadociv = fields.Selection([('Casada(o)','Casada(o)'),('Divorciada(o)','Divorciada(o)'),('Soltera(o)','Soltera(o)'),('Conviviente','Conviviente')], string='Estado Civil:')
	x_ocupactual = fields.Char(string='Ocupacion actual:')
	x_centro_est = fields.Char(string='Centro(s) de estudios:')
	x_culminaste = fields.Selection([('Si','Si'),('No','No')], string='Culminaste tus estudios?:')
	x_teconsideras = fields.Text(string='En la industria de la belleza, te consideras?:')
	x_comollegaste = fields.Text(string='Como llegaste a nosotros?:')
	
	x_facebook = fields.Selection([('Si','Si'),('No','No')], string='Usa Facebook?:')
	x_twitter = fields.Selection([('Si','Si'),('No','No')], string='Usa twitter?:')
	
	x_referenciado = fields.Char(string='Referenciado por:')
	x_fechareg = fields.Date(string='Fecha de registro')
	x_bco = fields.Char(string='Banco :')
	x_nrocta = fields.Char(string='Nro. de cta (S/.):')
	x_titular = fields.Char(string='Titula cta :')
	x_idnrohijos = fields.One2many('open_cliente.nrohijos','x_id_nrohijos',string='Detalle hijos')
	x_distrito_usr = fields.Many2one('open_cliente.distrito',string='Distrito:',)
  	x_urb_usr = fields.Many2one('open_cliente.urb',string="Urbanización:") #S,domain=[('distrito','=', x_distrito)])
  	x_codpostal_usr = fields.Many2one('open_cliente.codigopostal',string="Código Postal:")
	
class nrohijos(models.Model):
	_name = "open_cliente.nrohijos"
	#name = fields.Char(string='Detalle hijos', )
	x_sexo = fields.Selection([('Mujer','Mujer'),('Hombre','Hombre')], string='Sexo:')
	x_edad = fields.Integer(string='Edad')
	x_grado = fields.Char(string='Grado')
	x_id_nrohijos = fields.Many2one('res.users',string='Detalle hijos')
