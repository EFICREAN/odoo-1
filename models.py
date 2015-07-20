# -*- coding: utf-8 -*-

from openerp import models, fields, api

# Cliente - res_partner

class res_partner(models.Model):
	_name = "res.partner"
	_inherit = "res.partner"

	x_genero = fields.Selection([('Mujer','Mujer'),('Hombre','Hombre')], string='Genero:')
	
	x_tipocont = fields.Selection([('C','C'),('No grato','No grato'),('P','P'),('Ccmp/Trafa','Comp/Trafa')], string='Tipo contacto:')
  	x_apellido1 = fields.Char(string='Apellido 1:')
	x_cod_cliente = fields.Char(string="Cod cliente",compute="_compu1")

	@api.one
	@api.constrains('x_genero','x_tipocont','x_apellido1','id')
	def _compu1(self):
		if not self.x_apellido1: # if string is empty then is false
			x_apellido1x = "Nulo"
		else:
			x_apellido1x = self.x_apellido1
		self.x_cod_cliente = '%s%s%s%s' % (str(self.x_tipocont),
						 str(self.x_genero),
							x_apellido1x[:4],str(self.id))

  	x_rebote= fields.Selection([('R1','Hard'),('R2','Soft')], string='Rebote:')
  	x_operador = fields.Selection([('o1','Movistar'),('o2','Claro'),('o3','Bitel'),('o4','Entel')],string='Operador:')
  	x_tipored= fields.Selection([('R1','RPC'),('R2','RPE')], string='Red privada:')
  	x_name1= fields.Char(string='Nombre 1:')
  	x_name2= fields.Char(string='Nombre 2:')
  	x_apellido2 = fields.Char(string='Apellido 2:')
  	x_email2 = fields.Char(string='Email 2:')
  	x_phone2 = fields.Char(string='Telefono fijo 2:')
  	x_movil2 = fields.Char(string='Movil adicional 1:')
  	x_movil3 = fields.Char(string='Movil adicional 2:')
  	x_tipodoc = fields.Char(string='Tipo documento de dentidad:')
  	x_nrodoc = fields.Char(string='Nro. de documento de identidad:')
  	x_nrodpto = fields.Char(string='Nro. dpto:')
  	x_refdir = fields.Text(string='Referencia dirección:')
	urb_id = fields.Many2one('open_cliente.urb',string="Urbanización:")
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
	x_exp_servicio = fields.Boolean(string="Experiencia con este servicio?:")
	x_exp_delivery = fields.Boolean(string="Experiencia con SPA con Delivery?:")
	x_servicio_casa = fields.Text(string="Que tipo de servicio recibio en casa?:")
	x_usa_internet = fields.Boolean(string="Usa internet?:")
	x_recibir_prom = fields.Boolean(string="Desea recibir promociones en su correo?:")
	x_usa_fb = fields.Boolean(string= "Usa Facebook?:")
	x_interes_internet = fields.Text(string= "Interes internet:")
	x_usa_twitter = fields.Boolean(string= "Usa Twitter?:")
	ocupacion_id = fields.Many2one('open_cliente.ocupacion',string="Ocupación Actual")
	
	x_job = fields.Char(string="Empresa en la que trabaja:")	
	x_job_sector = fields.Char(string="Sector de la empresa:")	
	x_job_puesto = fields.Char(string="Puesto actual:")	
	x_carrera = fields.Char(string="Profesión:")	
	x_estadocivil = fields.Selection([('E1','Solero(a)'),('E2','Casado(a)'),('E3','Viudo(a)'),('E4','Divorciado(a)'),('E5','Separado(a)'),('E6','Conviviente')],string="Estado civil:")	
	x_nrohijos = fields.Integer(string="Nro. de hijos:")	
	Detalle_por_hijo = fields.One2many('open_cliente.hijos','hijo_id', String="Detalle por hijo")

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
	x_genero = fields.Selection([('S1',"Masculino"),('S2','Femenino')],string='Genero hijos', zise=15)
	x_edad = fields.Integer(string='Edad')
	x_grado = fields.Char(string='Grado academico',zise=25)
	hijo_id = fields.Many2one('res.partner',string='hola')

# Beauty trainer
class beauty_tr(models.Model):
	_name = "beauty.trainer"
	x_name_bt = fields.Char(string="Nombre")
	x_id_bt = fields.Integer(string="id_bt", compute = "_compu2")
	@api.one
	def _compu2(self):
		if not self.any() : # if is empty then is false
			self.x_id_bt = 1
		else:
			self.x_id_bt = self.x_id_bt.max() + 1

		

