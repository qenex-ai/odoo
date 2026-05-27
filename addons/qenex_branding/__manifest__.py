{
    'name': 'QENEX Branding',
    'summary': 'Replace Odoo brand surfaces with QENEX.',
    'description': """
QENEX Branding
==============
Drop-in rebrand of the Odoo Community web client, login page, browser tab,
favicon, PWA manifest, default email templates, and report letterheads.

Developer-facing namespaces (Python package `odoo`, model names, XML IDs,
table names) are deliberately left untouched.
    """,
    'version': '19.0.1.0.0',
    'category': 'Customizations',
    'author': 'QENEX Systems',
    'website': 'https://qenex.ai',
    'license': 'LGPL-3',
    'depends': ['web', 'mail'],
    'data': [
        'data/ir_config_parameter.xml',
        'data/res_partner_data.xml',
        'data/mail_templates.xml',
        'views/webclient_templates.xml',
        'views/report_templates.xml',
    ],
    'assets': {
        'web._assets_primary_variables': [
            ('prepend', 'qenex_branding/static/src/scss/primary_variables.scss'),
        ],
        'web.assets_backend': [
            'qenex_branding/static/src/scss/fonts.scss',
            'qenex_branding/static/src/scss/backend.scss',
            'qenex_branding/static/src/js/dialog_patch.js',
            'qenex_branding/static/src/js/title_part.js',
            'qenex_branding/static/src/xml/about_dialog.xml',
            'qenex_branding/static/src/xml/upgrade_dialog.xml',
        ],
        'web.assets_frontend': [
            'qenex_branding/static/src/scss/fonts.scss',
            'qenex_branding/static/src/scss/login.scss',
        ],
    },
    'post_init_hook': 'post_init_hook',
    'auto_install': True,
    'application': False,
    'installable': True,
}
