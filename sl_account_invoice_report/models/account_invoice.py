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
from dateutil.relativedelta import relativedelta
from datetime import datetime

class Account_Invoice_Report(models.Model):

    _inherit = 'account.invoice'
    @api.multi
    def print_invoice2(self):
        return self.env['report'].get_action(self,'sl_account_invoice_report.report_invoice2')

    @api.multi
    def print_boleta(self):
        return self.env['report'].get_action(self, 'sl_account_invoice_report.report_boleta')

    boleta_invoice = fields.Selection([('boleta', 'Boleta'), ('invoice', 'Factura')], "Tipo documento", related="journal_id.boleta_invoice")

    day = fields.Char('Día',compute = '_day')
    month = fields.Char('Mes',compute = '_month')
    month_number = fields.Char('Mes',compute='_month_number')
    year = fields.Char('Año',compute = '_year')
    ruc = fields.Char('Ruc',compute = '_ruc')

    @api.depends('day','date_invoice')
    def _day(self):
        if self.date_invoice:
            date_invoice = str(self.date_invoice)
            self.day = date_invoice[8:]

    @api.depends('month', 'date_invoice')
    def _month(self):
        meses = ('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo',
                 'Junio', 'Julio', 'Agosto', 'Setiembre', 'Octubre', 'Noviembre', 'Diciembre')

        if self.date_invoice:
            date_invoice = str(self.date_invoice)
            month_num = int(date_invoice[5:7])
            self.month = meses[month_num-1]

    @api.depends('month_number', 'date_invoice')
    def _month_number(self):
        if self.date_invoice:
            date_invoice = str(self.date_invoice)
            self.month_number = date_invoice[5:7]

    @api.depends('year', 'date_invoice')
    def _year(self):
        if self.date_invoice:
            date_invoice = str(self.date_invoice)
            self.year = date_invoice[2:4]

    @api.depends('ruc','partner_id.vat')
    def _ruc(self):
        if self.partner_id.vat:
            self.ruc = self.partner_id.vat[3:]

