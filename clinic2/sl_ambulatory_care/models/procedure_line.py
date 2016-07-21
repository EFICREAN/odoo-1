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

class Ambulatory_Procedure_Line(models.Model):
    _name = 'clinic.procedure.line'

    @api.model
    def _get_default_name(self):
        return self.env['ir.sequence'].get('clinic.procedure.line')

    name = fields.Char(string="Código linea procedimeinto", default=_get_default_name)
    ambulatory_id = fields.Many2one('clinic.ambulatory', 'Cuidado ambulatorio')
    procedure_id = fields.Many2one('clinic.procedure', 'Procedimiento')
    description = fields.Text('Descripción')

class Clinic_Ambulatory_Procedures(models.Model):
    _inherit = 'clinic.ambulatory'

    procedure_line_ids = fields.One2many('clinic.procedure.line', 'ambulatory_id', 'Procedimientos')