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

class Clinic_Appointment_Extend(models.Model):
    _inherit = 'medical.appointment'

    appointment_date = fields.Datetime('Fecha y hora', required=True, default=fields.Datetime.now())
    state = fields.Selection(
        [('draft','Nueva'),('reserv','Reservada'),('confirm','Confirmada'),('waiting','Espera'),
         ('process','en Ejecución'),('done','Realizado'),('cancel','Cancelado')], 'Estado', default='draft'
    )

    duration = fields.Float('Duración', default=15.00)

    @api.one
    def draft_reserv(self):
        self.write({'state':'reserv'})
        return True

    @api.one
    def reserv_confirm(self):
        self.write({'state':'confirm'})
        return True

    @api.one
    def confirm_wainting(self):
        self.write({'state': 'waiting'})
        return True

    @api.one
    def wainting_process(self):
        self.write({'state': 'process'})
        return True

    @api.one
    def process_done(self):
        self.write({'state': 'done'})
        return True

    @api.one
    def done_process(self):
        self.write({'state': 'process'})
        return True

    @api.one
    def to_cancel(self):
        self.write({'state': 'cancel'})
        return True


