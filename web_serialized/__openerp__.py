# -*- coding: utf-8 -*-
{
    'name': 'Trobz Web Serialized Field',
    'version': '1.0',
    'category': 'Hidden',
    'description': """
Add support for fields.serialized in from view with a new widget: "serialized"
    """,
    'author': 'Trobz',
    'website': 'https://github.com/trobz/openerp-widget-serialized',
    'depends': [
        'web_unleashed'
    ],
    
    'data': [
    ],
    
    'qweb' : [
        'static/src/templates/*'
    ],
    
    
    'css' : [
        'static/lib/jsoneditor/jsoneditor.css',
    
        'static/src/css/field_serialized.css',
    ],
       
    'js': [
        # lib
        'static/lib/jsoneditor/lib/jsonlint/jsonlint.js',
        'static/lib/jsoneditor/jsoneditor.js',
        
        'static/src/js/field_serialized.js'
    ],
    
    'test': [
    ]
}