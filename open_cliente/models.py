# -*- coding: utf-8 -*-

from openerp import models, fields, api

class res_partner(models.Model):
	_name = "res.partner"
	_inherit = "res.partner"
	x_tipocont = fields.Selection([('C1','C'),('C2','No grato'),('C3','P'),('C4','Comp/Trafa')], string='Tipo contacto:')
	x_genero = fields.Selection([('C1','Mujer'),('C2','Hombre')], string='Genero:')
	x_name1= fields.Char(string='Nombre 1:')
  	x_name2= fields.Char(string='Nombre 2:')
  	
  	x_apellido1 = fields.Char(string='Apellido 1:')
  	x_apellido2 = fields.Char(string='Apellido 2:')
  	x_tipodoc = fields.Char(string='Tipo documento de dentidad:')
  	x_nrodoc = fields.Char(string='Nro. de documento de identidad:')
  	
  	x_nrodpto = fields.Char(string='Nro. dpto:')
  	urb_id = fields.Many2one('open_cliente.urb',string="Urbanización:")		
  	x_refdir = fields.Text(string='Referencia dirección:')
  	x_email2 = fields.Char(string='Email 2:')
  	
  	x_phone2 = fields.Char(string='Telefono fijo 2:')
  	x_movil2 = fields.Char(string='Movil adicional 1:')
  	x_movil3 = fields.Char(string='Movil adicional 2:')
  	x_rebote= fields.Selection([('R1','Hard'),('R2','Soft')], string='Rebote:')
  	x_operador = fields.Selection([('o1','Movistar'),('o2','Claro'),('o3','Bitel'),('o4','Entel')],string='Operador:')
  	x_tipored= fields.Selection([('R1','RPC'),('R2','RPE')], string='Red privada:')
  
	x_edadini = fields.Char(string='Edad con la que nos conoció:')
	x_enc1 = fields.Text(string="Como se entero de nosotros?:")
	x_nombrerec = fields.Char(string="Quien nos recomendo?:")
	x_lugarprimeraexp = fields.Char(string="Lugar de primera experiencia:")
	
	x_campanna = fields.Char(string="Campaña de primera experiencia:")
	x_canalprimercontac = fields.Char(string="Canal del primer contacto:")
	x_fechaprimercon = fields.Char(string="Fecha primer contacto:")	
	
	x_primerprodcon = fields.Many2one('product.product',string="Primer producto consutado:")	
	x_subcateg_prim = fields.Many2one('product.category',string="Sub categoría 1er prod.:")
	x_categ_prim = fields.Many2one('product.category',string="Categoría 1er prod.")
	
	x_segunprodcon = fields.Many2one('product.product',string="Segundo producto consutado:")	
	x_subcateg_segun = fields.Many2one('product.category',string="Sub categoría 2do prod.:")
	x_categ_segun = fields.Many2one('product.category',string="Categoría 2do produc.:")

	x_obsnecesidad = fields.Text(string="Observación necesidad:")
	x_rpta_consultas = fields.Text(string="Respuesta a consulta:")
	x_eval_postcom = fields.Text(string="Evaluación post comunicación:")
	x_servicio_casa = fields.Text(string="Que tipo de servicio recibio en casa?:")
	
	x_exp_servicio = fields.Boolean(string="Experiencia con este servicio?:")
	x_exp_delivery = fields.Boolean(string="Experiencia con SPA con Delivery?:")
	x_usa_internet = fields.Boolean(string="Usa internet?:")
	x_recibir_prom = fields.Boolean(string="Desea recibir promociones en su correo?:")
	
	x_usa_fb = fields.Boolean(string= "Usa Facebook?:")
	x_usa_twitter = fields.Boolean(string= "Usa Twitter?:")
	x_interes_internet = fields.Text(string= "Interes internet:")
	ocupacion_id = fields.Many2one('open_cliente.ocupacion',string="Ocupación Actual")
	x_job = fields.Char(string="Empresa en la que trabaja:")	

	x_job_sector = fields.Char(string="Sector de la empresa:")	
	x_job_puesto = fields.Char(string="Puesto actual:")	
	x_carrera = fields.Char(string="Profesión:")	
	x_estadocivil = fields.Selection([('E1','Solero(a)'),('E2','Casado(a)'),('E3','Viudo(a)'),('E4','Divorciado(a)'),('E5','Separado(a)'),('E6','Conviviente')],string="Estado civil:")	
	x_nro_hijos = fields.Integer(string="Nro. de hijos:")	
	x_hijores_partner_id = fields.One2many('open_cliente.hijos','hijo_id', String="Detalle por hijo")

class urb(models.Model):
	_name = "open_cliente.urb"
	name = fields.Char(string='Urbanización')
	res_partner_id = fields.One2many('res.partner','urb_id', String="Urbanización")
	

class ocupacion(models.Model):
	_name = "open_cliente.ocupacion"
	name = fields.Char(string='Ocupación')
	oc_res_partner_id = fields.One2many('res.partner','ocupacion_id', String="Ocupación")

class hijos(models.Model):
	_name = "open_cliente.hijos"
	x_genero = fields.Selection([('S1',"Masculino"),('S2','Femenino')],string='genero')
	x_edad = fields.Integer(string='Edad')
	x_grado = fields.Char(string='Grado academico')
	hijo_id = fields.Many2one('res.partner', String="Hijo")
