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

class Clinic_Prescription_Line(models.Model):
    _name = 'clinic.prescription.line'

    @api.model
    def _get_default_name(self):
        return self.env['ir.sequence'].get('clinic.prescription.line')

    name = fields.Char(string="Código linea medicamento", default=_get_default_name)
    patient_id = fields.Many2one('medical.patient', 'Paciente', required=True)
    medicament_id = fields.Many2one('medical.medicament', string="Medicamento", required=True)
    indication_medicament = fields.Text(string="Indicación")
    medication_dosage_id = fields.Many2one('medical.medication.dosage', string="Dósis")
    note = fields.Text(string='Observaciones')
    date = fields.Datetime(string="Fecha", default=fields.Datetime.now())

    consult_id = fields.Many2one(comodel_name='clinic.consult', string="Consulta")

    #hospitalized_id = fields.Many2one(comodel='evaluation.lines', string="Hospitalización")


    physician_id = fields.Many2one('medical.physician', 'Médico')
    prescription_order_id = fields.Many2one(comodel_name='medical.prescription.order', string='Receta', ondelete='cascade')


