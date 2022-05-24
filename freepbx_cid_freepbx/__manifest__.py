# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Attendances Custom',
    'version': '1.0',
    'category': 'Human Resources/Attendances',
    'sequence': 240,
    'summary': 'Track employee attendance Custom',
    'description': """
       """,
    'website': 'https://www.odoo.com',
    'depends': ['hr_attendance'],
    'data': [
        'views/res_config_settings_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3',
}
