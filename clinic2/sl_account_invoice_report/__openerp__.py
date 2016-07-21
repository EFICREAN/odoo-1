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
        'sl_account_invoice_report.xml',
        'sl_account_invoice.xml',
        'views/account_invoice_report_view.xml',
        'sl_account_journal.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
