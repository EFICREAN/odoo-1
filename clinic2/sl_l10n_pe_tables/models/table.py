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


class TableTable(models.Model):
    _name = "table.table"

    name = fields.Char(
        string='Nombre'
    )
    code = fields.Char(
        string='Código'
    )
    description = fields.Text(
        string='Descripción'
    )


class TableType(models.Model):
    _name = "table.type"

    name = fields.Char(
        string='Nombre'
    )
    code = fields.Char(
        string='Código'
    )
    description = fields.Text(
        string='Descripción'
    )