from odoo.addons.qenex_branding.hooks import strip_powered_by_odoo


def post_init_hook(env):
    strip_powered_by_odoo(env, [
        'auth_signup.set_password_email',
        'auth_signup.mail_template_data_unregistered_users',
        'auth_signup.mail_template_user_signup_account_created',
        'auth_signup.portal_set_password_email',
    ])
