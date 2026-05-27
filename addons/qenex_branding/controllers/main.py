"""Serve /favicon.ico from the qenex_branding asset path.

Browsers and link previewers request the bare path; without this route
they would hit a 404 (Odoo's web.layout points <link rel="icon"> at our
asset path, but the root /favicon.ico is not aliased anywhere).
"""
from odoo import http
from odoo.tools import file_open


class QenexFavicon(http.Controller):

    @http.route('/favicon.ico', type='http', auth='public', methods=['GET'], readonly=True)
    def favicon(self):
        with file_open('qenex_branding/static/src/img/favicon.ico', 'rb') as f:
            return http.request.make_response(
                f.read(),
                headers=[
                    ('Content-Type', 'image/vnd.microsoft.icon'),
                    ('Cache-Control', 'public, max-age=86400'),
                ],
            )
