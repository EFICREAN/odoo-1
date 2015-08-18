## -*- coding: utf-8 -*-

from openerp import models, fields, api

# Sales - res_partner

class res_partner(models.Model):
	_name = "res.partner"
	_inherit = "res.partner"

		
#Nuevos campos
#Empresa
	x_tipocont = fields.Selection([('Cliente','Cliente'),('Prospecto','Prospecto'),('Comercial','Comercial'),
		('Competencia','Competencia'),('C-Corp','C-Corp'),('Com-Corp','Com-Corp'),('Comp-Corp','Comp-Corp'),
		('No grato-Corp','No grato-Corp'),('P-Corp','P-Corp')], string='Tipo contacto:')
  	
	x_cod_empresa = fields.Char(string='Código empresa:')
	x_tam_empresa = fields.Selection([('Grande','Grande'),('Mediana','Mediana'),('Pequeña','Pequeña')], string='Tamaño empresa:')
	x_categ_ind = fields.Many2one('open_cliente.categ_ind',string="Industria/categoría:")
	x_refdir = fields.Text(string='Referencia dirección:')
	x_direccion2 = fields.Text(string='Otras direcciones de interes:')
	x_twitter = fields.Char(string= "Twitter:")
	x_linkedln = fields.Char(string= "linkedln:")
	x_fb = fields.Char(string= "Facebook:")
	x_obs_emp = fields.Text(string="Observación sobre la empresa:")
	x_nroofi = fields.Char(string='Nro. oficina:')
	x_distrito = fields.Many2one('open_cliente.distrito',string="Distrito")
  	x_urb_id = fields.Many2one('open_cliente.urb',string="Urbanización:") #S,domain=[('distrito','=', x_distrito)])
  	x_codpostal_id2 = fields.Many2one('open_cliente.codigopostal',string="Código Postal:")
  	x_obs_emp_cont = fields.Text(string='Observación empresa/contacto:')

#Cliente
	x_genero = fields.Selection([('Mujer','Mujer'),('Hombre','Hombre')], string='Genero:')
	x_cod_contacto = fields.Char(string='Código contacto:')
	x_name1= fields.Char(string='Nombre 1:')
  	x_name2= fields.Char(string='Nombre 2:')
  	x_apellido1 = fields.Char(string='Apellido 1:')
  	x_apellido2 = fields.Char(string='Apellido 2:')
	x_dpto_contacto = fields.Char(string='Departamento de contacto:')
	x_evento_origen = fields.Char(string='Evento/origne de contacto:')
	x_evento_por = fields.Char(string='Evento recomendado por:')
	x_email = fields.Char(string='Email 2:')
	x_fecha_primer = fields.Date(string='Fecha primer contacto:')
	x_mobil1 = fields.Char(string='Movil adicional 1:')
	x_mobil2 = fields.Char(string='Movil adicional 2:')
	x_ss_corp_consultados = fields.Char(string='Servicios corporativos consultados:')
	x_nro_personas = fields.Integer(string='Nro. personas atender:')


class categ_ind(models.Model):
	_name = "open_cliente.categ_ind"
	name = fields.Char(string='Industria/categoría:')
	res_partner_id = fields.One2many('res.partner','x_categ_ind', string="Industria/categoría")

	
class urb(models.Model):
	_name = "open_cliente.urb"
	name = fields.Char(string='Urbanización')
	distrito = fields.Char(string='Distrito')
	res_partner_id = fields.One2many('res.partner','x_urb_id', string="Urbanización")
	
class distrito(models.Model):
	_name = "open_cliente.distrito"
	name = fields.Char(string='Distrito')
	codigo = fields.Char(string='codigo')
	x_distrito_id = fields.One2many('res.partner','x_distrito', string="Distrio")
	
class codpostal(models.Model):
	_name = "open_cliente.codigopostal"
	name = fields.Char(string='Código postal:')
	distrito = fields.Char(string='Distrito:')
	res_partner_id = fields.One2many('res.partner','x_codpostal_id2', string="Código Postal")
	





