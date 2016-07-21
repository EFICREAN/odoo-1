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


class Patient_bf(models.Model):
    #triage_ids = fields.One2many(
    #    'patient.triage',
    #    'patient_id',
    #    'Triage'
    #)
    _name = 'patient.biological_functions'

    patient_id = fields.Many2one('medical.patient','Paciente', required=True)
    date = fields.Datetime("Fecha y hora", default=fields.Datetime.now())
    bf_appetite = fields.Selection([('b', 'Bien'), ('r', 'Regular'), ('m', 'Mal')], 'Apetito')
    bf_thirst = fields.Selection([('b', 'Bien'), ('r', 'Regular'), ('m', 'Mal')], 'Sed')
    bf_stool = fields.Selection([('b', 'Bien'), ('r', 'Regular'), ('m', 'Mal')], 'Deposiciones')
    bf_urine = fields.Selection([('b', 'Bien'), ('r', 'Regular'), ('m', 'Mal')], 'Orina')