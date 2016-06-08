# -*- coding: utf-8 -*-

from openerp import models, fields, api


class part_sms(models.Model):
    	_name = "part.sms"
    	_inherit = "part.sms"

	nostop = fields.Boolean('NoStop', help='Do not display STOP clause in the message, this requires that this is not an advertising message')
