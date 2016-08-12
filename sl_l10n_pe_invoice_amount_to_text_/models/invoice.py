# -*- encoding: utf-8 -*-

import amount_to_text_PE
from openerp import models,fields, api

class account_invoice(models.Model):
    _inherit = 'account.invoice'

    #amount_to_text = fields.Char(string='Monto a Texto', size=256, help="Monto de la factura a letreas")
    amount_to_text = fields.Char(string='Monto a Texto', store=True, size=256, help="Monto de la factura a letreas", compute='_get_amount_to_text')
    @api.depends('amount_total')
    #@api.multi
    def _get_amount_to_text(self):
        for invoice in self:
            amount_to_text = amount_to_text_PE.get_amount_to_text(
                self, invoice.amount_total, 'es_cheque', 'code' in invoice. \
                                                         currency_id._columns and invoice.currency_id.code or invoice. \
                                                         currency_id.name)
            self.amount_to_text = amount_to_text
        return



