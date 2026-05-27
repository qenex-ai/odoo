"""Override the OdooBot intro message sent to each new user.

Stock copy is "Odoo's chat helps employees…". We replace it with a
QENEX-voice line: confident, precise, no exclamation marks.
"""
from markupsafe import Markup

from odoo import _, models


class ResUsers(models.Model):
    _inherit = 'res.users'

    def _init_odoobot(self):
        # Reimplement instead of super() to keep the message body under
        # our control. Mirrors the upstream behaviour: open a chat between
        # user and partner_root, post a transient intro, flag onboarding.
        self.ensure_one()
        odoobot_id = self.env['ir.model.data']._xmlid_to_res_id("base.partner_root")
        channel = self.env['discuss.channel']._get_or_create_chat([odoobot_id, self.partner_id.id])
        message = Markup("%s<br/>%s<br/><b>%s</b> <span class=\"o_odoobot_command\">:)</span>") % (
            _("Hello,"),
            _("QENEX Discuss is your team's internal chat. Send an emoji to begin."),
            _("Try sending me an emoji"),
        )
        channel.sudo().message_post(
            body=message,
            author_id=odoobot_id,
            message_type="comment",
            subtype_xmlid="mail.mt_comment",
            silent=True,
        )
        self.sudo().odoobot_state = 'onboarding_emoji'
