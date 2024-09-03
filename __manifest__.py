{
    'name': 'Hospital Management',
    'version': '17.0.0.1.0',
    'category': '',
    'license': 'LGPL-3',
    'author': 'Omar Sameh',
    'depends': ['base', 'mail', 'crm'
                ],
    'data': [
        'security/ir.model.access.csv',
        'views/main_menu.xml',
        'views/patient_view.xml',
        'views/appointment_view.xml',

    ],
    'demo': [],
    'application': True,
}