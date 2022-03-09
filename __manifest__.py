# -*- coding: utf-8 -*-
{
    'name': "booking_order_zhafron_10",

    'summary': """
        Booking Order Zhafron""",

    'description': """
        Booking Order Zhafron
    """,

    'author': "Zhafron",
    'website': "https://github.com/tickernelz",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Sales',
    'version': '1,0',
    'installable': True,
    'application': True,

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
    ],
}
