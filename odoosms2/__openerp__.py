# -*- coding: utf-8 -*-
{
    'name': "odoo sms v2",

    'summary': "Modulos para fines educativos",

    'description': "Modulos para fines educativos",

    'author': "Paul Orellana",
    'website': "www.facebook.com/odooerpperu",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'odoosms'],

    # always loaded
    'data': [
    #    "security/groups.xml",
    #    "security/ir.model.access.csv"
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
    'installable' : True,
    'application' : True,
    'auto_install': False,
}
