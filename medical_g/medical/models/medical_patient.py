# -*- coding: utf-8 -*-
# #############################################################################
#
# Tech-Receptives Solutions Pvt. Ltd.
# Copyright (C) 2004-TODAY Tech-Receptives(<http://www.techreceptives.com>)
# Special Credit and Thanks to Thymbra Latinoamericana S.A.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# #############################################################################
from openerp import models, fields, api
from datetime import datetime
from openerp.tools.translate import _
from dateutil.relativedelta import relativedelta


class MedicalPatient(models.Model):
    '''
    The concept of Patient included in medical.
    '''
    _name = 'medical.patient'
    _description = 'Medical Patient'
    _inherits = {'res.partner': 'partner_id', }

    @api.one
    def _compute_age(self):
        """
        age computed depending of the birth date of the
        membership request
        """
        now = datetime.now()
        if self.dob:
            dob = fields.Datetime.from_string(self.dob)

            if self.deceased:
                dod = fields.Datetime.from_string(self.dod)
                delta = relativedelta(dod, dob)
                deceased = _(' (deceased)')
            else:
                delta = relativedelta(now, dob)
                deceased = ''
            years_months_days = str(delta.years) + _('y ') + str(
                delta.months) + _('m ') + str(delta.days) + _('d')\
                + deceased
        else:
            years_months_days = _('No DoB !')
        self.age = years_months_days

    @api.one
    def action_invalidate(self):
        self.active = False
        self.partner_id.active = False

    age = fields.Char(compute='_compute_age')
    identification_code = fields.Char(
        string='Internal Identification',
        help='Patient Identifier provided by the Health Center.'
        '(different from the Social Security Number)')
    general_info = fields.Text(string='General Information')
    dob = fields.Date(string='Date of Birth')
    dod = fields.Datetime(string='Deceased Date')
    active = fields.Boolean(default=True)
    deceased = fields.Boolean()
    partner_id = fields.Many2one(
        comodel_name='res.partner', required=True, ondelete='cascade',
        index=True)
    gender = fields.Selection(
        selection=[
            ('m', 'Male'),
            ('f', 'Female'),
        ])
    medical_center_id = fields.Many2one(
        comodel_name='res.partner',
        domain="[('is_institution', '=', True)]",
        string='Medical Center'
    )
    marital_status = fields.Selection(
        selection=[
            ('s', 'Single'),
            ('m', 'Married'),
            ('w', 'Widowed'),
            ('d', 'Divorced'),
            ('x', 'Separated'),
            ('z', 'law marriage'),
        ])

    @api.model
    @api.returns('self', lambda value: value.id)
    def create(self, vals):
        vals['is_patient'] = True
        if not vals.get('identification_code'):
            sequence = self.env['ir.sequence'].get('medical.patient')
            vals['identification_code'] = sequence
        return super(MedicalPatient, self).create(vals)
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
	
	y_parto = fields.Selection([('EUTOCICO','EUTOCICO'),('CESAREA','CESAREA')],string='PARTO:')
	y_lactancia = fields.Selection([('MATERNA','MATERNA'),('MIXTA','MIXTA'),('FORMULA','FORMULA')],string='LACTANCIA:')
	y_desarrollo = fields.Selection([('NORMAL','NORMAL'),('ANORMAL','ANORMAL'),('FORMULA','FORMULA')],string='DESARROLLO:')
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
	x_abortos = fields.Char(string="ABORTOS")
	x_drogas = fields.Char(string="DROGAS")
	x_nro_parejas_12M = fields.Char(string="N° PAREJAS EN 12 MESES")

#(4) INMUNOLÓGICOS
	x_cartilla_vacunacion = fields.Selection([('COMPLETA','COMPLETA'),('INCOMPLETA','INCOMPLETA'),('NO TIENE','NO TIENE')],string='TIENE CARTILLA DE VACUNACIÓN:')
	x_ref_vacunacion_completa = fields.Selection([('SI','SI'),('NO','NO'),('NO RECUERDA','NO RECUERDA')],string='REFIERE VACUNACIÓN COMPLETA:')
	
#(5) EPIDEMIOLOGICOS
	x_tipo_vivienda = fields.Char(string="TIPO DE VIVIENDA")
	x_nro_personas_habitacion = fields.Char(string="N° PERSONAS / HABITACIÓN")
	x_ocupacion = fields.Char(string="OCUPACIÓN")
	x_viajes = fields.Char(string="VIAJES")
	
	y_Luz = fields.Selection([('SI','SI'),('NO','NO')],string='LUZ:')
	y_agua = fields.Selection([('SI','SI'),('NO','NO')],string='AGUA:')
	y_desague = fields.Selection([('SI','SI'),('NO','NO')],string='DESAGÚE:')
	x_medicamentos_uso_cont = fields.Text(string='MEDICAMENTOS DE USO CONTINUO:')
	
	x_asma = fields.Selection([('SI','SI'),('NO','NO')],string='ASMA:')
#Hoja de afiliación
	x_dni = fields.Integer(string="DNI:")
	x_lugar_nac = fields.Char(string="Lugar de Nacimiento:")
	x_estado_civil = fields.Selection([('S','S'),('C','C'),('V','V'),('D','D')],string='Estado Civil:')
	x_ocupacion = fields.Char(string='Ocupación:')
	x_raza = fields.Char(string='Raza:')
	x_grado_instruccion= fields.Char(string = 'Grado de instrucción:')
	x_religion = fields.Char(string='Religión:')
	x_nombre_padre = fields.Char(string='Nombre del padre:')
	x_apellido_padre = fields.Char(string='Apellido del padre:')
	x_nombre_madre = fields.Char(string='Nombre de la madre:')
	x_apellido_madre = fields.Char(string='Apellido de la madre:')
	x_otros = fields.Text(string = 'Otros :')
#Afiliación
	#Detalle_por_hijo = fields.One2many('open_cliente.hijos','hijo_id', String="Detalle por hijo")
	x_id_funciones_vitales = fields.One2many('funciones.vitales','id2_funciones_vitales',string="Funciones Vitales")

class funvitales(models.Model):
	_name = "funciones.vitales"
	x_dia = fields.Date(string="DIA:")
	x_hora = fields.Datetime(string="HORA:")
	x_pediatrico =  fields.Boolean(string="PEDIATRICO:")
	x_adulto =  fields.Boolean(string="ADULTO:")
	x_presion = fields.Char(string="PRESION ARTERIAL(mmgh)")
	X_frecuencia_card = fields.Char(string="FRECUENCIA CARDIACA(por minuto):")
	X_respiracion = fields.Char(string="RESPIRACIÓN(por minutos):")
	x_glicenia_tipo = fields.Selection([('HIPOGLICENIA','HIPOGLICENIA'),('HIPERGLICENIA','HIPERGLICENIA')],"GLICENIA TIPO:")
	x_glicenia_cant = fields.Char(string="GLICENIA (Mg/dl):")
	x_temperatura = fields.Integer(string="TEMPERATURA:")
	x_saturacion = fields.Char(string="SATURACION OXIGENO:")
	X_escala_dolor = fields.Selection([('0-Muy contento sin dolor'.'0-Muy contento sin dolor'),('2-Siente sólo un poquito de dolor','2-Siente sólo un poquito de dolor'),('4-Siente un poco más de dolor','4-Siente un poco más de dolor'),('6-Siente aún más dolor','6-Siente aún más dolor'),('8-Siente mucho dolor','8-Siente mucho dolor'),('10-El dolor es intenso','10-El dolor es intenso')], string="ESCALA DE DOLOR:")
	id2_funciones_vitales = fields.Many2one('medical.patient',string='Funciones Vitales')
	
	
#class appointment(models.Model):
#	_name = "medical.patient"
#	_inherit = "medical.patient"

#	name = fields.Char(
 #   		string='Name',
  #  		default=lambda self: self._get_default_name(),
#	)

#	@api.model
#	def _get_default_name(self):
 #   	return "test"	

