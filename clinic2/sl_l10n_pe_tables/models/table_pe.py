# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2016-TODAY Luis Paredes para http://www.softlabperu.com
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
############################################################################
from openerp import models, fields, api


class TablePe02(models.Model):
    _name = "table.pe.02"
    _inherits = {'table.table': 'table_id'}

    code_table_02 = fields.Char(
        string='Código tabla 02'
    )
    active = fields.Boolean(
        string='Activo',
        default=True
    )
    table_id = fields.Many2one(
        comodel_name='table.table',
        required=True,
        ondelete='cascade',
        index=True
    )
    name_short = fields.Char(
        string='Nombre corto'
    )
    date_expired = fields.Date(
        string='Fecha expiración'
    )
    description = fields.Text(
        'Descripción'
    )

    @api.multi
    @api.depends('name', 'code_table_02')
    def name_get(self):
        result = []
        for table in self:
            l_name = table.code_table_02 and table.code_table_02 + ' - ' or ''
            l_name += table.name
            result.append((table.id, l_name))
        return result