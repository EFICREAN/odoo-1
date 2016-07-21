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

class Clinic_Procedure_Lines(models.Model):
    _name = 'clinic.procedure.line1'

    @api.model
    def _get_default_name(self):
        return self.env['ir.sequence'].get('clinic.procedure.line')

    name = fields.Char(string='Código procedimiento', default=_get_default_name)
    patient_id = fields.Many2one(comodel_name='medical.patient', string='Paciente', required=True)
    date = fields.Datetime(string="Fecha", default=fields.Datetime.now())
    physician_id = fields.Many2one(comodel_name='medical.physician', string='Médico')
    description = fields.Text(string='Descripción')
    procedure_id = fields.Many2one(
        comodel_name='clinic.procedure', required=True, index=True, string='Procedimiento')
    state = fields.Selection(
        [('new','Solicitado'),('program', 'Programado'),('done', 'Realizado'), ('cancel', 'Anulado')], 'Estado procedimiento', default='new'
    )

