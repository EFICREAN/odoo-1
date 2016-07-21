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

class Admission_Plan_Line(models.Model):

    _name = 'plan.line'

    patient_id = fields.Many2one('medical.patient', 'Paciente')
    description = fields.Text(string="Descripción")
    inpatient_admission_id = fields.Many2one(comodel_name='inpatient.admission', string="Hospitalización")
    physician_id = fields.Many2one(comodel_name='medical.physician', string='Médico')
    date_registration = fields.Datetime(comodel_name="Fecha de registro", default=fields.Datetime.now())
    evaluation_line = fields.Many2one(comodel_name = 'evaluation.lines', string="Evolución")