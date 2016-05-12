# -*- coding: utf-8 -*-

from openerp import models, fields, api

class res_partner(models.Model):
	_name = "res.partner"
	_inherit = "res.partner"
#Antecedentes familiares	
	x_asma = fields.Selection([('Si','No')],string='ASMA:')
	x_diabetes = fields.Selection([('Si','No')],string='DIABETES:')
	x_cancer = fields.Selection([('Si','No')],string='CANCER:')
	x_hipertencion = fields.Selection([('Si','No')],string='HIPERTENSIÓ:')
	x_e_infecciosas = fields.Selection([('Si','No')],string='ENFERMEDADES INFECTOCONTAGIOSAS:')
	x_e_cardiovasculares = fields.Selection([('Si','No')],string='ENFERMEDADES CARDIOVASCULARES:')
	x_alergias = fields.Selection([('Si','No')],string='ALERGIAS:')
	x_padres_vivos = fields.Selection([('Si','No')],string='PADRES VIVOS:')
	x_otros = fields.Selection([('Si','No')],string='OTROS:')
	x_especifique = fields.Char(string="ESPECIFIQUE")

#Antecedentes Personales (Patologicos)
	
	y_asma = fields.Selection([('Si','No')],string='ASMA:')
	y_diabetes = fields.Selection([('Si','No')],string='DIABETES:')
	y_cancer = fields.Selection([('Si','No')],string='CANCER:')
	y_hipertencion = fields.Selection([('Si','No')],string='HIPERTENSIÓ:')
	y_e_infecciosas = fields.Selection([('Si','No')],string='ENFERMEDADES INFECTOCONTAGIOSAS:')
	y_e_cardiovasculares = fields.Selection([('Si','No')],string='ENFERMEDADES CARDIOVASCULARES:')
	y_alergias = fields.Selection([('Si','No')],string='ALERGIAS:')
	y_padres_vivos = fields.Selection([('Si','No')],string='PADRES VIVOS:')
	y_otros = fields.Selection([('Si','No')],string='OTROS:')
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

