# -*- encoding: utf-8 -*-
###########################################################################
#    Copyright (c) 2013 AACONSULTING - http://www.consulting-sac.com.pe/
#    All Rights Reserved.
#    info AACONSULTING (info@consulting-sac.com.pe)
############################################################################
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

{
    'name' : "sl_l10n_pe_invoice_amount_to_text_",
    'version' : "8.0",
    'depends' : ["account"],
    'author' : "Paul Orellana",
    'category' : "Localization/Peru",
    'description' : """Modulo para agregar el monto en texto customizado para implantación de versión 8.0 de ODOO
    """,
    'website' : "",
    'license' : "AGPL-3",
    'init_xml' : [],
    'demo_xml' : [],
    'update_xml' : [
    ],
    'data': ['views/invoice.xml'],
    'installable' : True,
    'active' : False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
