# -*- coding: utf-8 -*-

from openerp import models, fields, api

# Cliente - res_partner

class pos_config_dat(models.Model):
	_name = "pos.config"
	_inherit = "pos.config"

	x_dir_local = fields.Char(string="Direccion Local:")

