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


class AccountSequence(models.Model):

    _inherit = 'account.invoice'

    number = fields.Char(
        related='move_id.name',
        store=True,
        readonly=True,
        copy=False,
        states={'open': [('readonly', False), ('required', True)]})

    #cambiar a metodo write
    @api.multi
    def onchange_number(self, number=False):
        if number and self.move_id:
            move = self.move_id
            move.write({
                'name':number,
                'ref': number,
            })
