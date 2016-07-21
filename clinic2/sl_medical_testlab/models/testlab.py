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

class Patient_Testlab(models.Model):

    _name = 'clinic.testlab'

    @api.model
    def _get_default_name(self):
        return self.env['ir.sequence'].get('clinic.testlab')

    name = fields.Char('Código prueba laboratorio', default=_get_default_name)
    patient_id = fields.Many2one('medical.patient', 'Paciente', required=True)
    physician_id = fields.Many2one('medical.physician', 'Médico')
    date = fields.Datetime("Fecha y hora", default=fields.Datetime.now())
    testtype_id = fields.Many2one(
        comodel_name='clinic.testtype', required=True, index=True, string='Tipo exámen')
    state = fields.Selection(
        [('draft','Solicitado'), ('process','Programado'), ('done','Realizado'),
         ('cancel','Cancelado')], 'Estado', default='draft'
    )
    test_attach_line = fields.One2many('clinic.test.attachment', 'testlab_id', 'Adjuntos')

    @api.one
    def draft_program(self):
        self.write({'state':'process'})
        return True

    @api.one
    def program_done(self):
        self.write({'state':'done'})
        return True

    @api.one
    def done_program(self):
        self.write({'state':'process'})
        return True

    @api.one
    def to_cancel(self):
        self.write({'state': 'cancel'})
        return True

    @api.one
    def cancel_program(self):
        self.write({'state': 'process'})
        return True