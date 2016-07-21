{
    'name': 'Odoo consult report',
    'version': '8.0.1.1.0',
    'category': 'Clinic',
    'depends': [
        'sl_medical_consult',
        'sl_prescription_report'
    ],
    'author': 'Luis Paredes para Softlab Perú SAC',
    'website': 'http://www.softlabperu.com',
    'license': 'AGPL-3',
    'data': [
        'sl_consult_report.xml',
        'views/consult_report_view.xml',

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
