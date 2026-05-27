"""De-brand stray Odoo references in the OdooBot conversational script.

The bot's reply strings live in `mail_bot.MailBot._get_answer`. The full
script is a long if/elif tree; rather than fork it, we wrap the answer
and run a single substitution on the way out.
"""
import re

from odoo import models

_ODOO_INLINE = re.compile(r'\bOdoo\b')


class MailBot(models.AbstractModel):
    _inherit = 'mail.bot'

    def _get_answer(self, channel, body, values, command=False):
        ans = super()._get_answer(channel, body, values, command=command)
        if ans:
            ans = _ODOO_INLINE.sub('QENEX', ans)
        return ans
