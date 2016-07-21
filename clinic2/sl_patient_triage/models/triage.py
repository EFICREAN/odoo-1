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


class Patient_Triage(models.Model):

    _name = 'patient.triage'

    @api.model
    def _get_default_name(self):
        return self.env['ir.sequence'].get('patient.triage')

    name = fields.Char(string="Código",required=True, default=_get_default_name)
    patient_id = fields.Many2one('medical.patient','Paciente', required=True)
    date = fields.Datetime("Fecha y hora", default=fields.Datetime.now())
    pediatric = fields.Boolean("Pediátrico")
    adult = fields.Boolean("Adulto")
    blood_pressure = fields.Char("[PA] Presión arterial",required=True)
    frecuence_card = fields.Char("[FC] Frecuencia cardiaca (/min)")
    respiration = fields.Char("Respiración (/min)")
    glycemia_ammount = fields.Char("Glicemia")
    temperature_ammount = fields.Integer('[T] Temperatura (°C)')
    temp_type = fields.Selection([('febril', 'Febril'), ('afebril', 'Afebril')],default='afebril', string='Tipo')
    saturation_oxigen = fields.Char("[SatO] Saturacion oxigeno")
    weight = fields.Char("Peso")
    size = fields.Char("Talla")
    escale_plain = fields.Selection([('va_0', '0-Muy contento sin dolor'),
                                       ('val_2', '2-Siente sólo un poquito de dolor'),
                                       ('val_4', '4-Siente un poco más de dolor'),
                                       ('val_6', '6-Siente aún más dolor'),
                                       ('val_8', '8-Siente mucho dolor'),
                                       ('val_10', '10-El dolor es intenso')], string="Escala dolor")


