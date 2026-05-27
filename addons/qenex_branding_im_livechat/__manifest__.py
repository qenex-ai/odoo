{
    'name': 'QENEX Branding — Live Chat',
    'summary': 'Strip Odoo branding from livechat support page and email.',
    'version': '19.0.1.0.0',
    'author': 'QENEX Systems',
    'website': 'https://qenex.ai',
    'license': 'LGPL-3',
    'category': 'Customizations',
    'depends': ['qenex_branding', 'im_livechat'],
    'data': [
        'data/im_livechat_templates.xml',
    ],
    'auto_install': True,
}
