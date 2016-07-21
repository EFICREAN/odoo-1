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

class Clinic_pediatric_vaccine(models.Model):

    _name = 'clinic.pediatric.vaccine'

    #@api.model
    #def _get_default_name(self):
    #    return self.env['ir.sequence'].get('clinic.pediatric')
    #name = fields.Char(string="Código cirugía", default=_get_default_name)

    newborn_id = fields.Many2one('clinic.pediatric.newborn',"Nombre del bebe")

    name = fields.Char('Nombre de la vacuna')
    dosis = fields.Integer('Dosis')
    v_date = fields.Datetime(string="Fecha", default=fields.Datetime.now())
    medical_center = fields.Many2one('res.partner','Centro médico',domain="[('is_company' = True)]")
    physician_id = fields.Many2one('medical.physician', 'Médico')
    note = fields.Text('Obseraciones')