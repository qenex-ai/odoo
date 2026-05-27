{
    'name': 'QENEX Branding — CRM Partner Assign',
    'summary': 'Strip Odoo branding from partner-assign lead forward emails.',
    'version': '19.0.1.0.0',
    'author': 'QENEX Systems',
    'website': 'https://qenex.ai',
    'license': 'LGPL-3',
    'category': 'Customizations',
    'depends': ['qenex_branding', 'website_crm_partner_assign'],
    'auto_install': True,
    'post_init_hook': 'post_init_hook',
}
