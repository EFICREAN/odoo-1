{
    'name': 'Odoo prescription report',
    'version': '8.0.1.1.0',
    'category': 'Clinic',
    'depends': [
        'medical'
    ],
    'author': 'Luis Paredes para Softlab Perú SAC',
    'website': 'http://www.softlabperu.com',
    'license': 'AGPL-3',
    'data': [

        'sl_prescription_report.xml',
        'views/prescription_report_view.xml',

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
