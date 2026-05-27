{
    'name': 'QENEX Branding — Digest',
    'summary': 'Strip Odoo branding from digest emails (footer + mobile banner).',
    'version': '19.0.1.0.0',
    'author': 'QENEX Systems',
    'website': 'https://qenex.ai',
    'license': 'LGPL-3',
    'category': 'Customizations',
    'depends': ['qenex_branding', 'digest'],
    'data': [
        'data/digest_templates.xml',
    ],
    'auto_install': True,
}
