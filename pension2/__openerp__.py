# -*- coding: utf-8 -*-
{
    'name': "pension2",

    'summary': "Modulos para fines educativos",

    'description': "Modulos para fines educativos",

    'author': "Paul Orellana",
    'website': "www.facebook.com/odooerpperu",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates2.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}
