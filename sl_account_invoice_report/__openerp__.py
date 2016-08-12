{
    'name': 'Odoo invoice report',
    'version': '8.0',
    'category': 'invoice',
    'depends': [
        'account',
        'sl_l10n_pe_invoice_amount_to_text_'
    ],
    'author': 'Paul Orellan',
    'website': '',
    'license': 'AGPL-3',
    'data': [
        'sl_account_invoice_report.xml',
        'views/sl_account_invoice.xml',
        'views/account_invoice_report_view.xml',
        'views/sl_account_journal.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
