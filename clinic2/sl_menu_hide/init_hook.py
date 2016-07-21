# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    This module copyright (C) 2015 Therp BV <http://therp.nl>.
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
from openerp import SUPERUSER_ID
from openerp.api import Environment


def post_init_hook(cr, pool):
    env = Environment(cr, SUPERUSER_ID, {})
    adjust_menu(env)


def adjust_menu(env):
    group_original_menu_id = env.ref('sl_menu_hide.group_original_menu').id
    menus = [
        'base.menu_reporting',
        'hr.menu_hr_root',
        'knowledge.menu_document',
        'stock.menu_stock_root',
        # 'medical.medical_root'
    ]

    for menu_ref in menus:
        try:
            menu = env.ref(menu_ref)
            menu.write({
                'groups_id': [(6, 0, [group_original_menu_id])]
            })
        except:
            pass
