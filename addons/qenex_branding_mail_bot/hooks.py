"""On install: rewrite existing OdooBot messages so users already in the DB
also see QENEX-branded text, not just freshly-created accounts.
"""
import logging
import re

_logger = logging.getLogger(__name__)

_ODOO_INLINE = re.compile(r'\bOdoo\b')
_INTRO_NEEDLE = "chat helps employees"


def post_init_hook(env):
    odoobot = env.ref('base.partner_root', raise_if_not_found=False)
    if not odoobot:
        return
    Message = env['mail.message'].sudo()
    n = 0
    for msg in Message.search([('author_id', '=', odoobot.id)]):
        body = msg.body or ''
        if not body or 'Odoo' not in body:
            continue
        new = _ODOO_INLINE.sub('QENEX', body)
        if new != body:
            msg.write({'body': new})
            n += 1
    _logger.info("qenex_branding_mail_bot: rewrote %d OdooBot messages", n)
