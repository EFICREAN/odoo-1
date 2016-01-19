## -*- coding: utf-8 -*-

from openerp import models, fields, api

class btr_enc(models.Model):
        _name = "open_cliente.btr_enc"
	name  = fields.Date(string='Fecha encuesta:')
	x01	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Cepillado de cabello :')				
	x02	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Planchado de cabello :')				
	x03	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Corte cabello hombre :')				
	x04	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Corte cabello mujer :')				
	x05	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Rizado / ondas de cabello :')				
								
	x07	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Decoloración de vellos :')				
	x08	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Depilación  Corporal con cera :')				
	x09	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Depilación  Corporal laser :')				
	x10	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Depilación  facial con hilo Hindu :')				
								
	x12	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Colocación  de pestañas:')				
	x13	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Extensiones de pestañas pelo a pelo:')				
	x14	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Rizado de pestañas:')				
	x15	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Teñido  de pestañas :')				
	x16	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Teñido  de cejas :')				
	x17	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Planchado de cejas :')				
								
	x19	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Manicure con diseño :' )				
	x20	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Manicure frances / americano :')				
	x21	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Pedicure con diseño :' ) 				
	x22	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Pedicure frances / americano :')				
	x23	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Uso de parafina para manos y pies :')				
	x24	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Podología geriatrica :')				
	x25	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Podología ortopedica :')				
	x26	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Podología preventiva :')				
								
	x28	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Peinado para novias :')				
	x29	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Peinados para fiestas :')				
	x30	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Maquillaje para fiestas :')				
	x31	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Maquillaje para novias :')				
	x32	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Maquillaje para teens :')				
	x33	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Maquillaje publicitario :')				
	x34	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Otros servicios COSMETOLOGICOS que maneja(s) :')				
								
								
	x37	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Cobertura / exfoliación Corporal para el aclaramiento / manchas :')				
	x38	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Cobertura / exfoliación   Corporal para  la hidratación :')
	x39	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Cobertura / exfoliación  Corporal para mejorar la textura :')				
								
	x41	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Masaje descontracturante en camilla :')				
	x42	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Masaje Shiatsu en camilla :')				
	x43	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Masajes con piedras calientes en camilla :')				
	x44	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Masajes relajantes en camilla :')				
	x45	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Masajes relajantes en silla :')				
	x46	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Masajes corporales  para reducir medidas :')				
	x47	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Masajes corporales para reafirmar / tonificar medidas :')				
	x48	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Masajes corporales anticelulitico :')				
	x49	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Masajes corporales antiestrias :')				
	x50	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Drenaje linfatico corporal :')				
	x51	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Drenaje linfatico facial :')				
	x52	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Reflexología de pies :')				
	x53	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Reflexología de manos :')				
								
	x55	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Faciales para hidratar :')				
	x56	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Faciales para reafirmar/tonificar :')				
	x57	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Faciales para reducir / aclarar manchas :')				
	x58	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Faciales para reducir arrugas :')				
	x59	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Implantes / rellenos faciales (Acido hialuronico) :')				
	x60	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Implantes / rellenos faciales (Plaquetas de plasma) :')				
								
	x62	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Maquillaje permanente de camuflaje :')				
	x63	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Maquillaje permanente pelo a pelo :')				
	x64	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Maquillaje permanente tradicional :')				
	x65	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Maquillaje permanente tridimensional :')				
								
	x67	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Venta de aromatizadores, quemadores y similares :')				
	x68	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Venta de bloqueadores/paneles solares :')				
	x69	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Venta de productos de belleza para el cuerpo :')				
	x70	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Venta de productos de belleza para el rostro :')				
	x71	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Otros servicios COSMEATRICOS que maneja(s) :')				
								
								
								
	x75	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Instrumentos Cosmetologícos:')				
	x76	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Secadora de cabello :')				
	x77	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Plancha de cabello :')				
	x78	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Instrumentos Cosmeatricos :')				
	x79	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Puntas de Diamante :')				
	x80	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Ultra Cavitación :')				
	x81	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Ultra sonido :')				
	x82	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Vacum :')				
	x83	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Vaporizador :')				
	x84	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Piedras calientes :')				
	x85	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Dermografo :')				
	x86	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Centrifuga :')				
	x87	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Altafrecuencia :')				
	x88	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Electroporación')				
	x89	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Endermologie :')				
	x90	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Gimnasia pasiva :')				
	x91	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Manta termica :')				
	x92	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Maquina de Radio Frecuencia (RF) :')				
	x93	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Otra(s) maquina(s) :')				
								
								
								
	x97	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Experiencia atendiendo mujeres embarazadas :')				
	x98	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Experiencias atendiendo caballeros(hombres) :')				
	x99	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Experiencia atendiendo ancianos(as) :')				
	x100	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Experiencia atendiendo adolescentes (teens) :')				
	x101	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Experiencia atendiendo pacientes luego de una cirugia plastica :')				
	x102	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Experiencia atendiendo a ejecutivos o gerentes :')				
	x103	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Experiencia trabajado en eventos masivos (ferias, full day, etc) :')				
	x104	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Experiencia en jornadas de 8 ó horas continuas :')				
	x105	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Experiencia liderando/dirigiendo grupos (2 a 5 personas) :')				
	x106	=	fields.Selection([('Basica','Basica'),('Media','Media'),('Alta','Alta')],	string='Experiencia trabajando a domicilio :')				
	x_encuesta = fields.Many2one('res.users',string='Encuesta')
