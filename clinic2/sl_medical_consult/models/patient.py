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

class Clinic_Patient_Consult(models.Model):

    _inherit = 'medical.patient'

    consult_ids = fields.One2many(
        'clinic.consult',
        'patient_id',
        'Consulta'
        )
    prescription_ids = fields.One2many(
        'medical.prescription.order',
        'patient_id',
        'Receta'
    )
    sale_order_id = fields.Many2one(comodel_name='sale.order', string='Carrito de compra')

    @api.multi
    def print_medical_history(self):
        return self.env['report'].get_action(self, 'sl_medical_history_report.report_medical_history_view')
