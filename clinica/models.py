# -*- coding: utf-8 -*-

from openerp import models, fields, api

class res_partner(models.Model):
	_name = "medical.patient"
	_inherit = "medical.patient"
#Antecedentes familiares	
	x_asma = fields.Selection([('SI','SI'),('NO','NO')],string='ASMA:')
	x_diabetes = fields.Selection([('SI','SI'),('NO','NO')],string='DIABETES:')
	x_cancer = fields.Selection([('SI','SI'),('NO','NO')],string='CANCER:')
	x_hipertencion = fields.Selection([('SI','SI'),('NO','NO')],string='HIPERTENSIÓN:')
	x_e_infecciosas = fields.Selection([('SI','SI'),('NO','NO')],string='ENFERMEDADES INFECTOCONTAGIOSAS:')
	x_e_cardiovasculares = fields.Selection([('SI','SI'),('NO','NO')],string='ENFERMEDADES CARDIOVASCULARES:')
	x_alergias = fields.Selection([('SI','SI'),('NO','NO')],string='ALERGIAS:')
	x_padres_vivos = fields.Selection([('SI','SI'),('NO','NO')],string='PADRES VIVOS:')
	x_otros = fields.Selection([('SI','SI'),('NO','NO')],string='OTROS:')
	x_especifique = fields.Char(string="ESPECIFIQUE")

#Antecedentes Personales (Patologicos)
	
	y_asma = fields.Selection([('SI','SI'),('NO','NO')],string='ASMA:')
	y_diabetes = fields.Selection([('SI','SI'),('NO','NO')],string='DIABETES:')
	y_cancer = fields.Selection([('SI','SI'),('NO','NO')],string='CANCER:')
	y_hipertencion = fields.Selection([('SI','SI'),('NO','NO')],string='HIPERTENSIÓN:')
	y_e_infecciosas = fields.Selection([('SI','SI'),('NO','NO')],string='ENFERMEDADES INFECTOCONTAGIOSAS:')
	y_e_cardiovasculares = fields.Selection([('SI','SI'),('NO','NO')],string='ENFERMEDADES CARDIOVASCULARES:')
	y_alergias = fields.Selection([('SI','SI'),('NO','NO')],string='ALERGIAS:')
	y_padres_vivos = fields.Selection([('SI','SI'),('NO','NO')],string='PADRES VIVOS:')
	y_otros = fields.Selection([('SI','SI'),('NO','NO')],string='OTROS:')
	y_especifique = fields.Char(string="ESPECIFIQUE")
	y_operaciones_previas_frac = fields.Char(string="OPERACIONES PREVIAS Y FRACTURAS")
#Fisiologicos
	
	y_parto = fields.Selection([('EUTOCICO','EUTOCICO'),('CESAREA','CESAREA')],string='ASMA:')
	y_lactancia = fields.Selection([('MATERNA','MATERNA'),('MIXTA','MIXTA'),('FORMULA','FORMULA')],string='ASMA:')
	y_desarrollo = fields.Selection([('NORMAL','NORMAL'),('ANORMAL','ANORMAL'),('FORMULA','FORMULA')],string='ASMA:')
	# ALIMENTACION BAJA, MODERADA, ALTA
	
	y_carbohidratos = fields.Selection([('BAJA','BAJA'),('MODERADA','MODERADA'),('ALTA','ALTA')],string='CARBOHIDRATOS:')
	y_proteinas = fields.Selection([('BAJA','BAJA'),('MODERADA','MODERADA'),('ALTA','ALTA')],string='PROTEINAS:')
	y_grasas = fields.Selection([('BAJA','BAJA'),('MODERADA','MODERADA'),('ALTA','ALTA')],string='GRASAS:')
	y_azucares = fields.Selection([('BAJA','BAJA'),('MODERADA','MODERADA'),('ALTA','ALTA')],string='AZUCARES:')
	
	x_menarquia = fields.Char(string="MENARQUIA")
	x_alcohol = fields.Selection([('SI','SI'),('NO','NO')],string='ALCOHOL:')
	x_nro_parejas = fields.Char(string="N° PAREJAS")
	x_ritmo_catemenial = fields.Char(string="RITMO CATEMENIAL")
	x_cafe = fields.Char(string="CAFÉ")
	x_inicio_rrss = fields.Char(string="INICIO DE RRSS")
	x_embarazos = fields.Char(string="EMBARAZOS")
	x_tabaco = fields.Selection([('SI','SI'),('NO','NO')],string='TABACO:')
	x_nro_parejas_12M = fields.Char(string="N° PAREJAS EN 12 MESES")
	x_abortos = fields.Char(string="ABORTOS")
	x_drogas = fields.Char(string="DROGAS")
#(4) INMUNOLÓGICOS
	x_cartilla_vacunacion = fields.Selection([('COMPLETA','COMPLETA'),('INCOMPLETA','INCOMPLETA'),('NO TIENE','NO TIENE')],string='TIENE CARTILLA DE VACUNACIÓN:')
	x_ref_vacunacion_completa = fields.Selection([('SI','SI'),('NO','NO'),('NO RECUERDA','NO RECUERDA')],string='REFIERE VACUNACIÓN COMPLETA:')
	
#(5) EPIDEMIOLOGICOS
	x_tipo_vivienda = fields.Char(string="DROGAS")
	y_otros = fields.Selection([('SI','SI'),('NO','NO')],string='OTROS:')
	
