# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2016-TODAY Luis Paredes para http://www.softlabperu.com
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
from openerp import models, fields, api, exceptions


class PartnerTable02(models.Model):
    _inherit = 'res.partner'

    table_02_id = fields.Many2one(
        comodel_name='table.pe.02',
        string='Tipo documento',
        required=True
    )
    number_doc = fields.Char(
        string='Número',
        required=True
    )

    @api.multi
    def onchange_number_doc(self, number_doc=False, table_02_id=False):
        if number_doc and table_02_id:
            table02=self.env['table.pe.02']
            code_t_02=table02.browse(table_02_id).code
            if code_t_02=='6':
                return {'value': {
                    'vat': 'PER'+number_doc,
                    'is_company': True,
                    }}
            if code_t_02=='1':
                return {'value': {
                    'vat': 'PED'+number_doc,
                    'is_company': False,
                    }}

