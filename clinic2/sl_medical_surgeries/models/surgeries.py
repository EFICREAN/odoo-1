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

class Clinic_Surgeries(models.Model):
    _name = 'clinic.surgeries'

    @api.model
    def _get_default_name(self):
        return self.env['ir.sequence'].get('clinic.surgeries')

    name = fields.Char(string="Código cirugía", default=_get_default_name)
    patient_id = fields.Many2one('medical.patient','Paciente', required=True)
    physician1_id = fields.Many2one('medical.physician', 'Médico')
    physician2_id = fields.Many2one('medical.physician', 'Anastesista')
    date_init = fields.Datetime(string="Fecha y hora inicio", default=fields.Datetime.now())
    date_end = fields.Datetime(string="Fecha y hora fin", default=fields.Datetime.now())
    description = fields.Text('Descripción general')
    res_description = fields.Text('Descripción')
    res_anesthesia = fields.Text('Resumen anastecia')
    res_others = fields.Text('Otra información')
    sale_order_id = fields.Many2one(comodel_name='sale.order', string='Pedido')
    order_line = fields.One2many(comodel_name='sale.order.line', string='Detalle', related='sale_order_id.order_line', readonly=False)
    procedure_line_ids = fields.One2many(comodel_name = 'clinic.procedure.line1', inverse_name='surgeries_id', string= 'Procedimientos')
    state = fields.Selection(
        [('draft', 'Nueva'),('process', 'En proceso'), ('pay', 'Pagado'),
         ('done', 'Realizado'), ('cancel', 'Anulado')], 'Estado', default='draft'
    )

