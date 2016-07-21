# -*- coding: utf-8 -*-
##############################################################################
#
#    Softlab Perú SAC
#    Copyright (C) 2016-TODAY Tech-Receptives(<http://www.softlabperu.com>)
#    Special Credit and Thanks to Luis Paredes :D
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp import models, fields, api


class Patient_medical_history(models.Model):

    _inherit = 'medical.patient'

    fam_asthma = fields.Selection([('yes', 'Si'), ('no', 'No')], 'Asma', default='no')
    fam_cardiovascular = fields.Selection([('yes', 'Si'), ('no', 'No')], 'Enfermedades cardiovasculares',default='no')
    fam_diabetic = fields.Selection([('yes', 'Si'), ('no', 'No')], 'Diabetes', default='no')
    fam_allergy = fields.Selection([('yes', 'Si'), ('no', 'No')],'Alergias', default='no')
    fam_cancer = fields.Selection([('yes', 'Si'), ('no', 'No')], 'Cancer', default='no')
    fam_living_parents= fields.Selection([('yes', 'Si'), ('no', 'No')], 'Padres vivos', default='no')
    fam_hypertension = fields.Selection([('yes', 'Si'), ('no', 'No')], 'Hipertensión', default='no')
    fam_infectious = fields.Selection([('yes', 'Si'), ('no', 'No')], 'Enfermedades infectocontagiosas',default='no')
    #fam_others = fields.Text('Otros')
    fam_specify = fields.Text('Especifique')


    per_asthma = fields.Selection([('yes', 'Si'), ('no', 'No')], 'Asma', default='no')
    per_cardiovascular = fields.Selection([('yes', 'Si'), ('no', 'No')], 'Enfermedades cardiovasculares', default='no')
    per_diabetic = fields.Selection([('yes', 'Si'), ('no', 'No')], 'Diabetes', default='no')
    per_allergy = fields.Selection([('yes', 'Si'), ('no', 'No')], 'Alergias', default='no')
    per_cancer = fields.Selection([('yes', 'Si'), ('no', 'No')], 'Cancer', default='no')
    per_living_parents = fields.Selection([('yes', 'Si'), ('no', 'No')], 'Padres vivos', default='no')
    per_hypertension = fields.Selection([('yes', 'Si'), ('no', 'No')], 'Hipertensión', default='no')
    per_infectious = fields.Selection([('yes', 'Si'), ('no', 'No')], 'Enfermedades infectocontagiosas', default='no')
    #per_others = fields.Text('Otros')
    per_specify = fields.Text('Especifique')
    per_previous_operations_frac = fields.Char('Operaciones previas y fracturas')


# Fisiologicos - physiological

    ph_birth = fields.Selection([('eutocico', 'Eutocico'), ('cesarea', 'Cesarea')], 'Parto')
    ph_lactation = fields.Selection([('materna', 'Materna'), ('mixta', 'Mixta'), ('formula', 'Formula')],
                               'Lactancia')
    ph_development = fields.Selection([('normal', 'Normal'), ('anormal', 'Anormal')],'Desarrollo')

# ALIMENTACION BAJA, MODERADA, ALTA - feeding high, moderate and low

    fe_carbohydrates = fields.Selection([('bajo', 'Bajo'), ('moderado', 'Moderado'), ('alto', 'Alto')],'Carbohidratos')
    fe_proteins = fields.Selection([('bajo', 'Bajo'), ('moderado', 'Moderado'), ('alto', 'Alto')],'Proteinas')
    fe_grease = fields.Selection([('bajo', 'Bajo'), ('moderado', 'Moderado'), ('alto', 'Alto')], 'Grasas')
    fe_sugars = fields.Selection([('bajo', 'Bajo'), ('moderado', 'Moderado'), ('alto', 'Alto')], 'Azucares')
    fe_menarche = fields.Char('Menarquia')
    fe_alcohol = fields.Selection([('yes', 'Si'), ('no', 'No')],'Alcohol', default='no')
    fe_nro_couples = fields.Char('N° parejas')
    fe_catemenial_pace = fields.Char('Ritmo cateminial')
    fe_coffee = fields.Selection([('yes', 'Si'), ('no', 'No')],'Café', default='no')
    fe_start_rrss = fields.Char('Inicio de rrss:')
    fe_pregnancies = fields.Char('Embarazos')
    fe_tabacco = fields.Selection([('yes', 'Si'), ('no', 'No')],'Tabaco', default='no')
    fe_abortions = fields.Char('Abortos')
    fe_drugs = fields.Selection([('yes', 'Si'), ('no', 'No')],'Drogas', default='no')
    fe_nro_couples_12M = fields.Char('N° parejas en 12 meses')

# (4) INMUNOLÓGICOS - Immunological
    in_cartilla_vaccination = fields.Selection(
    [('completa', 'Completa'), ('incompleta', 'Incompleta'), ('no_tiene', 'No Tiene')],
    'Tiene cartilla de vacunación:')
    in_ref_vaccination_complete = fields.Selection([('yes', 'Si'), ('no', 'No'), ('no_recuerda', 'No recuerda')],
                                             'Refiere vacunación completa')

# (5) EPIDEMIOLOGICOS - epidemiologists
    ep_type_living_place = fields.Char('Tipo de vivienda')
    ep_nro_people_room = fields.Char('N° personas / hábitación')
    ep_occupation = fields.Char('Ocupación')
    ep_travel = fields.Char('Viajes')
    ep_light = fields.Selection([('si', 'Si'), ('no', 'No')], 'Luz', default='no')
    ep_water = fields.Selection([('si', 'Si'), ('no', 'No')], 'Agua', default='no')
    ep_drain  = fields.Selection([('si', 'Si'), ('no', 'No')], 'Desagüe', default='no')
    ep_continuous_use_medicines = fields.Text('Medicamentos de uso continuo')
    ep_asthma = fields.Selection([('si', 'Si'), ('no', 'No')],'Asma', default='no')
