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

class Patient_TestAttachment(models.Model):

    _name = 'clinic.test.attachment'

    @api.model
    def _get_default_name(self):
        return self.env['ir.sequence'].get('clinic.test.attachment')

    name = fields.Char(required=True, default=_get_default_name)
    description = fields.Char(string='Descripción')
    date = fields.Datetime("Hora", default=fields.Datetime.now())
    attachment_id = fields.Binary('Adjunto')
    testimage_id = fields.Many2one(comodel_name='clinic.testimage', string='Exámen imágen')
    testlab_id = fields.Many2one(comodel_name='clinic.testlab', string='Exámen laboratorio')

class Testlab_Attachmment(models.Model):

    _inherit = 'clinic.testlab'

    testlab_id = fields.One2many('clinic.testlab', 'testlab_id', 'Exámen laboratorio')

class Testimage_Attachmment(models.Model):

    _inherit = 'clinic.testimage'

    testimage_id = fields.One2many('clinic.testimage', 'testimage_id', 'Exámen imágen')

