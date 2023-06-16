# -*- coding: utf-8 -*-
{
    'name': "MSY RESTAURANT1",

    'summary': """MSY RESTAURANT1""",

    'description': """MSY RESTAURANT1""",
    'sequence':-100 ,
    'author': "KUDERBEK ARDAKTYM",
    'website': "",
    'category': 'Accounting/Accounting',
    'version': '1.1',


    # any module necessary for this one to work correctly
    'depends': ['base','hr'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/employee.xml',
        'views/addons.xml',
        'views/kitchen.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application' : True,
}
