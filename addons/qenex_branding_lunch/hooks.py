from odoo.addons.qenex_branding.hooks import strip_powered_by_odoo


def post_init_hook(env):
    strip_powered_by_odoo(env, [
        'lunch.lunch_order_mail_supplier',
    ])
