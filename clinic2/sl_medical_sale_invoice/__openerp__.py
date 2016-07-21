{
    'name': 'Comprobantes de venta',
    'version': '8.0.1.1.0',
    'category': 'Clinic',
    'depends': [
        'sale',
        'account'
    ],
    'author': 'Luis Paredes para Softlab Perú SAC',
    'website': 'http://www.softlabperu.com',
    'license': 'AGPL-3',
    'data': [
        'views/sale_view.xml',
        'views/account_invoice_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
