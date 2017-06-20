{
    'name' : 'Custom pos ticket odoo 10',
    'version' : '1.0.0',
    'author' : 'IT-Projects Peru, Paul Orellana',
    'license': 'GPL-3',
    'category' : 'Point Of Sale',
    'website' : '',
    'description': """

Tested on Odoo 10.0
    """,
    'depends' : ['point_of_sale'],
    'data':[
        ],
    'qweb': [
        'static/src/xml/pos.xml',
    ],
    'installable': True,
    'auto_install': False,
}
