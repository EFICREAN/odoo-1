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
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# #############################################################################

from openerp import api, fields, models

class Medical_Pathology_Clinic(models.Model):
    _inherit = 'medical.pathology'

    @api.multi
    def name_get(self):
        result = []
        for pathology in self:
            res_name = '[%s] %s' % (pathology.code or '', pathology.name)
            result.append((pathology.id, res_name))
        return result

    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        args = list(args or [])
        if name:
            search_name = name
        if operator != '=':
            search_name = '%s%%' % name
        vancancies = self.search([('code', operator, search_name)] + args,
                                 limit=limit)
        if vancancies.ids:
            return vancancies.name_get()
        return super(Medical_Pathology_Clinic, self)\
            .name_search(name=name, args=args, operator=operator, limit=limit)