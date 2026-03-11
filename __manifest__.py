{
    'name': 'Fixer',
    'version': '17.0.1.0.0',
    'depends': ['base', 'hr', 'contacts'],
    'data': [
        'security/ir.model.access.csv',
        'views/clients.xml',
        'views/jobtype.xml',
        'views/equipment.xml',
        'views/workman.xml',
        'views/job.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
}