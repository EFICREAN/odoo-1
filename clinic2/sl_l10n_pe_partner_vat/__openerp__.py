{
    'name': 'Ingreso de tipos de documentos de identidad',
    'version': '8.0.1.1.0',
    'category': 'peruvian',
    'depends': [
        'base',
        'base_vat',
        'sl_l10n_pe_tables',
    ],
    'author': 'Luis Paredes para Softlab Perú SAC',
    'website': 'http://www.softlabperu.com',
    'license': 'AGPL-3',
    'data': [
        'views/res_partner_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
