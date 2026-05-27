from odoo.addons.qenex_branding.hooks import strip_powered_by_odoo


def post_init_hook(env):
    # Demo-only template. Hook is a no-op when demo data is disabled.
    strip_powered_by_odoo(env, [
        'crm.mail_template_demo_crm_lead',
    ])
