from odoo.addons.qenex_branding.hooks import strip_powered_by_odoo


def post_init_hook(env):
    # All targets are demo records (mailing.mailing). When demo data is
    # disabled the lookup misses silently and the hook is a no-op.
    strip_powered_by_odoo(env, [
        'mass_mailing.mass_mail_1',
        'mass_mailing_crm.mass_mail_lead_0',
        'mass_mailing_sale.mass_mail_sale_order_0',
    ])
