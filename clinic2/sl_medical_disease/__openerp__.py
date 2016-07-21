{
    'name': 'Odoo clinic disease',
    'version': '8.0.1.1.0',
    'category': 'Clinic',
    'depends': [
        'medical',
        'medical_disease',
    ],
    'author': 'Luis Paredes para Softlab Perú SAC',
    'website': 'http://www.softlabperu.com',
    'license': 'AGPL-3',
    'data': [
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
