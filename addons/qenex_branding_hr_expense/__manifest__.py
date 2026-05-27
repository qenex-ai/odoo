{
    'name': 'QENEX Branding — Expenses',
    'summary': 'Strip Odoo branding from expense submission emails.',
    'version': '19.0.1.0.0',
    'author': 'QENEX Systems',
    'website': 'https://qenex.ai',
    'license': 'LGPL-3',
    'category': 'Customizations',
    'depends': ['qenex_branding', 'hr_expense'],
    'data': [
        'data/hr_expense_templates.xml',
    ],
    'auto_install': True,
}
