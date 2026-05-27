{
    'name': 'QENEX Branding — CRM',
    'summary': 'Strip Odoo branding from CRM demo mail templates.',
    'version': '19.0.1.0.0',
    'author': 'QENEX Systems',
    'website': 'https://qenex.ai',
    'license': 'LGPL-3',
    'category': 'Customizations',
    'depends': ['qenex_branding', 'crm'],
    'auto_install': True,
    'post_init_hook': 'post_init_hook',
}
