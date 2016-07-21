# -*- coding: utf-8 -*-
# #############################################################################
#
# Tech-Receptives Solutions Pvt. Ltd.
# Copyright (C) 2004-TODAY Tech-Receptives(<http://www.techreceptives.com>)
# Special Credit and Thanks to Thymbra Latinoamericana S.A.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# #############################################################################

from openerp import models, fields, api

class Clinic_Medical_Medicament(models.Model):
    _inherit = 'medical.medicament'

    @api.multi
    def name_get(self):
        res = []
        for rec in self:
            name = '%s - %s' % (rec.product_id.name, rec.code_medicament)
            res.append((rec.id, name))
        return res

    code_medicament = fields.Char('Código medicamento')
    description = fields.Text('Descripción')
    drug_form_id = fields.Many2one(
        comodel_name='medical.drug.form', string='Presentación', required=False)
