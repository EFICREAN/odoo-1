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

class Clinic_Procedure(models.Model):
    _name = 'clinic.procedure'
    _inherit = ['mail.thread']
    _inherits = {'product.product': 'product_id'}

    @api.multi
    def onchange_type(self, _type):
        return self.product_id.onchange_type(_type)

    @api.multi
    def onchange_uom(self, uom_id, uom_po_id):
        return self.product_id.onchange_uom(uom_id, uom_po_id)

    code_procedure = fields.Char('Código procedimiento')
    product_id = fields.Many2one(
        comodel_name='product.product', required=True, ondelete="cascade")
    description = fields.Text('Descripción')

    @api.model
    @api.returns('self', lambda value: value.id)
    def create(self, vals):
        vals['is_procedure'] = True
        return super(Clinic_Procedure, self).create(vals)

