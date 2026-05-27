from odoo.addons.qenex_branding.hooks import strip_powered_by_odoo


def post_init_hook(env):
    strip_powered_by_odoo(env, [
        'gamification.email_template_badge_received',
        'gamification.email_template_goal_reminder',
        'gamification.simple_report_template',
        'gamification.mail_template_data_new_rank_reached',
    ])
