{
    'name': 'QENEX Branding — Website Profile',
    'summary': 'Strip Odoo branding from forum profile validation email.',
    'version': '19.0.1.0.0',
    'author': 'QENEX Systems',
    'website': 'https://qenex.ai',
    'license': 'LGPL-3',
    'category': 'Customizations',
    'depends': ['qenex_branding', 'website_profile'],
    'auto_install': True,
    'post_init_hook': 'post_init_hook',
}
