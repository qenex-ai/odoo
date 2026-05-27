{
    'name': 'QENEX Branding — Auth Signup',
    'summary': 'Strip Odoo branding from signup/reset-password emails.',
    'version': '19.0.1.0.0',
    'author': 'QENEX Systems',
    'website': 'https://qenex.ai',
    'license': 'LGPL-3',
    'category': 'Customizations',
    'depends': ['qenex_branding', 'auth_signup'],
    'data': [
        'data/auth_signup_templates.xml',
    ],
    'auto_install': True,
    'post_init_hook': 'post_init_hook',
}
