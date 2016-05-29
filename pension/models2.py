# -*- coding: utf-8 -*-

from openerp import models, fields, api
from openerp.osv import osv

class custom_account(models.Model):
    _inherits = 'account.invoice'
    
x_dni2 = fields.Char(string="Dni padre")
@api.multi
def onchange_partner_id2(self, partner_id):
	if partner_id:
            p = self.env['res.partner'].browse(partner_id)
            self.x_dni2 = p.x_dni_padre
