from odoo import models
from odoo.http import request


class IrHttp(models.AbstractModel):
    _inherit = 'ir.http'

    def session_info(self):
        info = super().session_info()
        IrConfig = request.env['ir.config_parameter'].sudo()
        info['support_url'] = IrConfig.get_param(
            'web.support_url', default='mailto:support@qenex.ai'
        )
        return info
