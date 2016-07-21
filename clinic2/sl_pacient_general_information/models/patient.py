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

class Clinic_Patient_Appointment(models.Model):

    _inherit = 'medical.patient'

    identification_code = fields.Char('Historia Clínica N°', related="number_doc")
    number_contact=fields.Char('Tel/Cel. de responsable')

    kinship = fields.Char('Parentesco')

    ocupation = fields.Char('Ocupación')
    race = fields.Char('Raza')
    grade_instruction = fields.Selection(
            [('no_education', 'Sin educación'), ('incomplet_primary', 'Pimaria Incompleta'),('complet_primary', 'Pimaria Completa'),
             ('incomplet_secondary', 'Secundaria Incompleta'), ('completed_secondary', 'Secundaria Completa'),
             ('technical', 'Educación Técnica'), ('university', 'Educación Universitaria'),
             ('other', 'Otros') ],'Grado de instrucción')
    religion = fields.Char('Religión')

    name_father = fields.Char('Nombre del padre')
    name_lastname_father = fields.Char('Apellidos de padre')
    name_mother = fields.Char('Nombre de madre')
    name_lastname_mother = fields.Char('Apellidos madre')
    other_family = fields.Text('Otro familiar')


    @api.multi
    def name_get(self):
        result = []
        for patient in self:
            res_name = '[%s] %s' % (patient.identification_code or '', patient.name)
            result.append((patient.id, res_name))
        return result


    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        args = list(args or [])
        if name:
            search_name = name
        if operator != '=':
            search_name = '%s%%' % name
        vancancies = self.search([('identification_code', operator, search_name)] + args,
                                 limit=limit)
        if vancancies.ids:
            return vancancies.name_get()
        return super(Clinic_Patient_Appointment, self) \
            .name_search(name=name, args=args, operator=operator, limit=limit)