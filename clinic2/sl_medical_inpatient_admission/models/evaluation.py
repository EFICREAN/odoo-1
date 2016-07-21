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
from openerp.report import  report_sxw
from datetime import time, timedelta, datetime


class Evaluation_Lines(models.Model):

    _name = 'evaluation.lines'

    @api.model
    def _get_default_name(self):
        return self.env['ir.sequence'].get('evaluation.lines')

    name = fields.Char(required=True, default=_get_default_name, string="Código de evolución")
    physician_id = fields.Many2one('medical.physician', 'Médico')
    date_registration = fields.Datetime("Fecha de registro", default=fields.Datetime.now())
    patient_id = fields.Many2one('medical.patient', 'Paciente', required="True")

    esubject = fields.Text('Subjetivo',help="Como se sintio de un día para otro")
    eobject = fields.Text('Objetivo', help="Como se encuentra a nivel general")
    appreciation = fields.Text('Apreciación')

    inpatient_admission_id = fields.Many2one(comodel_name='inpatient.admission',string="Hospitalización")
    plan_line_ids = fields.One2many(comodel_name='plan.line', inverse_name='evaluation_line',
                                    string='Indicaciones Hospitalarias')
