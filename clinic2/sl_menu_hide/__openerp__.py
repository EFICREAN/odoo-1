# -*- encoding: utf-8 -*-
{
    "name": "Clinic menus hide",
    "version": "8.0.0.1.0",
    "author": "Luis Paredes para Softlab Perú SAC",
    "website": "",
    "license": "AGPL-3",
    "category": "clinic",
    "depends": [
        "base",
        "knowledge",
        "mail",
        "stock",
        # "medical"
    ],
    'data': [
        'security/kardex_menu_security.xml',
        'menu_data.xml'
        ],
    "post_init_hook": "post_init_hook",
    'installable': True
}
