{
    'name': 'Odoo invoice report',
    'version': '8.0.1.1.0',
    'category': 'Clinic',
    'depends': [
        'medical',
    ],
    'author': 'Luis Paredes para Softlab Perú SAC',
    'website': 'http://www.softlabperu.com',
    'license': 'AGPL-3',
    'data': [
        'account_invoice_report.xml',
        'account_invoice_custom.xml',
        'views/account_invoice_report_view.xml',
        'account_journal.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
