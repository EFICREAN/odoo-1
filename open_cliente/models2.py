## -*- coding: utf-8 -*-

from openerp import models, fields, api

# Sales - crm.lead

class crm_lead(models.Model):
	_name = "crm.lead"
	_inherit = "crm.lead"


	x_serv_corp = fields.Many2one('open_cliente.serv_corp',string="Servicios Corporativos:")
	x_nro_personas_at = fields.Integer(string="Nro Personas atender:")
	x_nro_horas_req = fields.Float(string="Nro de horas requeridas:")
	x_nro_dias_req = fields.Float(string="Nro de días requeridas:")
	x_tipo_evento = fields.Selection([('Ocasional','Ocasional'),('Frecuente','Frecuente')], string='Tipo Evento:')
	x_razon_realiza_evento = fields.Char(string='Razon para realizar el evento:')
	x_nombre_evento = fields.Many2one('open_cliente.nom_evento',string="Nombre del Evento:")
	x_visita = fields.Selection([('Si','Si'),('No','No')], string= 'Se visito a cliente?:')
	x_nivel_interes = fields.Selection([('Alto','Alto'),('Bajo','Bajo'),('Medio','Medio')], string= 'Nivel de interes:')

class serv_corp(models.Model):
	_name = "open_cliente.serv_corp"
	name = fields.Char(string='Servicios Corporativos:')
	id_serv_corp = fields.One2many('crm.lead','x_serv_corp', string="Servicios Corportativos:")

class product_categ(models.Model):
	_name = "product.category"
	_inherit = "product.category"

	x_cod_prod = fields.Char(string='Código categoría:')

# sales - product.product

class product_temp(models.Model):
	_name = "product.template"
	_inherit = "product.template"

	x_cod_prod2 = fields.Char(string='Código producto:')
	x_precio_8h = fields.Integer(string = 'Precio por módulo (8 horas):')
	x_min_std = fields.Integer(string='Minuto estandar por persona:')
	x_num_max_ps = fields.Integer(string='Número máximo de personas:')
	x_ambos_sexos = fields.Selection([('Si','Si'),('No','No')], string= 'Para ambos sexos?:')

#sales - sale.order
class sale_order(models.Model):
	_name = "sale.order"
	_inherit = "sale.order"
	
	x_nombre_evento = fields.Many2one('open_cliente.nom_evento',string="Nombre del Evento:")
	

#sales - account_invoice
class account_invoice(models.Model):
	_name = "account.invoice"
	_inherit = "account.invoice"
	
	x_nombre_evento = fields.Many2one('open_cliente.nom_evento',string="Nombre del Evento:")	
	x_forma_pago = fields.Selection([('Deposito','Deposito'),('Cheque','Cheque'),('Efectivo','Efectivo'),('Canje','Canje')], string= 'Forma de pago:')
	x_date_delivery = fields.Date(string='Fecha de entrega factura:')
	x_date_service = fields.Char(string='Fecha del servicio:')
	x_dia_service = fields.Char(string='Día del servicio:')
	x_dia_pago = fields.Selection([('Lunes','Lunes'),('Martes','Martes'),('Miercoles','Miercoles'),
									  ('Jueves','Jueves'),('Viernes','Viernes'),('Sábado','Sábado'),
									  ('Domingo','Domingo')], string= 'Día de pago:')
	
	x_lugar_service = fields.Char(string='Lugar servicio:')
	x_dias_credito = fields.Integer(string='Días de crédito:')
	x_costos_btt = fields.Float(string = 'Costo Beauty Trainer/ Transporte (S/.):')
	x_btt = fields.Many2many('res.users',string="Beauty Trainer:")

	#x_nro_horas = fields.Float(related='account.invoice.line.x_nro_horas',store=False)
	#x_dias = fields.Integer(related='account.invoice.line.x_dias',store=False)
	#x_q_modulos = fields.Integer(related='account.invoice.line.x_q_modulos',store=False)


class accont_invoice_line(models.Model):
	_name = 'account.invoice.line'
	_inherit = 'account.invoice.line'
	x_nro_horas = fields.Float(string="Nro horas")
	x_dias = fields.Integer(string="Nro días")
	x_q_modulos = fields.Integer(string="Cant. módulos")


class nom_evento(models.Model):
	_name = "open_cliente.nom_evento"
	name = fields.Char(string='Nombre del Evento:')
	id_nom_evento = fields.One2many('crm.lead','x_nombre_evento', string="Nombre del Evento:")
	