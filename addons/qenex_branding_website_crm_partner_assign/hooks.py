from odoo.addons.qenex_branding.hooks import strip_powered_by_odoo


def post_init_hook(env):
    strip_powered_by_odoo(env, [
        'website_crm_partner_assign.email_template_lead_forward_mail',
    ])
