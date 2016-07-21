{
    'name': 'Clinic surgeries',
    'version': '8.0.1.1.0',
    'category': 'Clinic',
    'depends': [
        'medical',
        'sale',
        'sl_clinic_procedure'
    ],
    'author': 'Luis Paredes para Softlab Perú SAC',
    'website': 'http://www.softlabperu.com',
    'license': 'AGPL-3',
    'data': [
        'data/ir_sequence.xml',
        'security/ir.model.access.csv'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
