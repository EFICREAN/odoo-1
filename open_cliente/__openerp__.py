# -*- coding: utf-8 -*-
{
    'name': "open_cliente",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Add new funtionality and modify forms for miaspa corporate 
    """,

    'author': "Your Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly   
    'depends': [
		'product',
		'base',
        'crm',
        'sale',
        'account'
		],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates1.xml',
        'templates2.xml',
        'res_users.xml',
        'res_users_enc.xml',
        'templates3.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml'
    ],
    'active': False,
    'installable':True,
    'application':True,
    'certificate':"",
}
