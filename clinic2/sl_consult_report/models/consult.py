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

class Clinic_Consul_Report(models.Model):

    _inherit = 'clinic.consult'

    @api.multi
    def print_EL(self):
        return self.env['report'].get_action(self,'sl_consult_report.report_consult_EL')

    @api.multi
    def print_IM(self):
        return self.env['report'].get_action(self, 'sl_consult_report.report_consult_IM')

    @api.multi
    def print_prescription(self):
        return self.env['report'].get_action(self, 'sl_prescription_report.report_prescription_view')
