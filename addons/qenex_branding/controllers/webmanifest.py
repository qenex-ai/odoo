"""Override the PWA webmanifest controller so colors, icons, and offline
icon path resolve to QENEX assets.

Inherits via subclassing; the original WebManifest class is replaced in the
HTTP routing table by virtue of being loaded after the `web` addon.
"""
from odoo.http import request
from odoo.addons.web.controllers.webmanifest import WebManifest


ICON_192 = '/qenex_branding/static/src/img/app-icon-192.png'
ICON_512 = '/qenex_branding/static/src/img/app-icon-512.png'
ICON_IOS = '/qenex_branding/static/src/img/app-icon-180.png'


def _param(env, key, default):
    return env['ir.config_parameter'].sudo().get_param(key, default)


class QenexWebManifest(WebManifest):

    def _get_webmanifest(self):
        env = request.env
        web_app_name = _param(env, 'web.web_app_name', 'QENEX')
        theme_color = _param(env, 'web.manifest_theme_color', '#0A0E27')
        background_color = _param(env, 'web.manifest_background_color', '#0A0E27')
        manifest = {
            'name': web_app_name,
            'scope': '/odoo',
            'start_url': '/odoo',
            'display': 'standalone',
            'background_color': background_color,
            'theme_color': theme_color,
            'prefer_related_applications': False,
            'icons': [
                {'src': ICON_192, 'sizes': '192x192', 'type': 'image/png'},
                {'src': ICON_512, 'sizes': '512x512', 'type': 'image/png'},
            ],
            'shortcuts': self._get_shortcuts(),
        }
        return manifest

    def _icon_path(self):
        return 'qenex_branding/static/src/img/app-icon-192.png'
