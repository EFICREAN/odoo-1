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

class Clinic_pediatric_newborn(models.Model):
    _name = 'clinic.pediatric.newborn'

    #@api.model
    #def _get_default_name(self):
    #    return self.env['ir.sequence'].get('clinic.pediatric')
    #name = fields.Char(string="Código cirugía", default=_get_default_name)
    vaccine_id = fields.One2many(
        'clinic.pediatric.vaccine',
        'newborn_id',
        'Vacunas'
    )
    name = fields.Char('Nombre del bebe')
    number_baby = fields.Char('Número identificación')
    patient_id = fields.Many2one('medical.patient','Madre', required=True)
    birthdate = fields.Datetime(string="Fecha de Nacimiento", default=fields.Datetime.now())
    medical_center = fields.Many2one('res.partner','Centro médico',domain="[('is_company' = True)]")
    physician1_id = fields.Many2one('medical.physician', 'Firmado por')
    sex = fields.Selection([('hombre','Hombre'),('mujer','Mujer')],string='Sexo')
    discharged = fields.Datetime(string="Fecha y hora de alta", default=fields.Datetime.now())
    physician2_id = fields.Many2one('medical.physician', 'Médico responsable')
    lenght = fields.Integer('Largo (cm)')
    cephalic_per = fields.Integer('Perimetro cefálico')
    weight = fields.Integer('Peso (kg)')
    congenital_disease = fields.Many2one('medical.pathology','Enfermedad congénita')
    note = fields.Text('Notas')
    #Hallazgo y prueba
    #Neonatal signos y sintomas
    menconum = fields.Boolean('Meconum')
    pos_barlow = fields.Boolean('Positive Barlow')
    amb_gen = fields.Boolean('Genitales Ambiguos')
    hematomas = fields.Boolean('Hematomas')
    tra_palmar_creaser = fields.Boolean('Pliegue palmar transversal')
    syndactily = fields.Boolean('Sindactilia')
    positive_ortolani = fields.Boolean('Ortolani positivo')
    hernia = fields.Boolean('Hernia')
    erbs_palsy = fields.Boolean('Paralisis de Erbs')
    talipes_eq = fields.Boolean('Equinovaro Talipes')
    polydactily = fields.Boolean('Polidactilia')

    state = fields.Selection(
        [('draft', 'Nueva'),('signed', 'Firmado')], 'Estado', default='draft'
    )

    @api.one
    def s_signed(self):
        self.write({'state': 'signed'})
        return True
