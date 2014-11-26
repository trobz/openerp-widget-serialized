# -*- coding: utf-8 -*-
{
    'name': 'Trobz Web Serialized Field',
    'version': '1.0',
    'category': 'Hidden',
    'description': """
Add support for fields.serialized in from view with a new widget: "serialized"

Note:

Odoo 8.0 doesn't support `fields.serialized` anymore, you have 
to install the server wide module `base_field_serialized` 
from https://github.com/OCA/server-tools OCA repository.
    """,
    'author': 'Trobz',
    'website': 'https://github.com/trobz/openerp-widget-serialized',
    'depends': [
        'web_unleashed'
    ],
    
    'data': [
        # JS/CSS Assets files
        'views/web_serialized.xml',
    ],
    
    'qweb' : [
        'static/src/xml/*'
    ]
}