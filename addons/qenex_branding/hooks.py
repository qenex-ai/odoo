"""Post-install hook: seed brand-aligned defaults on existing companies.

Only fills fields where the value is still the Odoo default — never clobbers
a value the operator has already set.
"""
import base64
import logging
import re
from pathlib import Path

from odoo import api, SUPERUSER_ID

_logger = logging.getLogger(__name__)

PRIMARY = '#6D28D9'
SECONDARY = '#22D3EE'
# In Odoo's mail layouts: email_secondary_color = button background,
# email_primary_color = button text. We want violet buttons with white
# text in transactional mail.
EMAIL_PRIMARY = '#FFFFFF'
EMAIL_SECONDARY = '#6D28D9'

ODOO_DEFAULT_PRIMARY = '#714B67'
ODOO_DEFAULT_SECONDARY = '#875A7B'


def _read_module_file(rel_path):
    here = Path(__file__).parent
    return (here / rel_path).read_bytes()


def post_init_hook(env):
    Company = env['res.company']
    companies = Company.search([])

    logo_png = base64.b64encode(_read_module_file('static/src/img/favicon-512.png'))

    for company in companies:
        vals = {}
        if not company.primary_color or company.primary_color.lower() == ODOO_DEFAULT_PRIMARY.lower():
            vals['primary_color'] = PRIMARY
        if not company.secondary_color or company.secondary_color.lower() == ODOO_DEFAULT_SECONDARY.lower():
            vals['secondary_color'] = SECONDARY
        # email_primary_color / email_secondary_color only exist with mail installed
        if 'email_primary_color' in company._fields and (
            not company.email_primary_color or company.email_primary_color.lower() == ODOO_DEFAULT_PRIMARY.lower()
        ):
            vals['email_primary_color'] = EMAIL_PRIMARY
        if 'email_secondary_color' in company._fields and (
            not company.email_secondary_color or company.email_secondary_color.lower() == ODOO_DEFAULT_SECONDARY.lower()
        ):
            vals['email_secondary_color'] = EMAIL_SECONDARY
        # Replace default Odoo company logo if untouched
        if 'uses_default_logo' in company._fields and company.uses_default_logo:
            vals['logo'] = logo_png
        if vals:
            company.write(vals)

    _logger.info("qenex_branding: applied brand defaults to %d companies", len(companies))


# --- shared helper used by companion qenex_branding_* modules ------------

# Matches the "Powered by <a …>Odoo</a>" anchor that recurs verbatim across
# 15+ stock mail templates. Tolerant of attribute order and surrounding
# whitespace. Captures nothing — used purely for replacement.
_POWERED_BY_ODOO_LINK = re.compile(
    r'Powered\s+by\s*<a\b[^>]*?(?:odoo\.com)[^>]*>\s*Odoo\s*</a>\s*\.?',
    re.IGNORECASE | re.DOTALL,
)
# Plain "Powered by Odoo" without the anchor (e.g. inside <strong> tags).
_POWERED_BY_ODOO_PLAIN = re.compile(
    r'Powered\s+by\s*(?:<strong>\s*)?Odoo(?:\s*</strong>)?\s*\.?',
    re.IGNORECASE,
)


def strip_powered_by_odoo(env, xmlids):
    """De-brand the ``body_html`` of any record carrying it.

    Works for ``mail.template``, ``mailing.mailing`` and any other model
    that exposes a ``body_html`` field. Looks up each xml-id; if the
    record is missing (companion installed but target uninstalled, or
    demo data disabled) we silently skip it.
    """
    for xmlid in xmlids:
        rec = env.ref(xmlid, raise_if_not_found=False)
        if not rec or 'body_html' not in rec._fields:
            continue
        body = rec.body_html or ''
        new_body = _POWERED_BY_ODOO_LINK.sub('', body)
        new_body = _POWERED_BY_ODOO_PLAIN.sub('', new_body)
        if new_body != body:
            rec.with_context(tracking_disable=True).write({'body_html': new_body})
            _logger.info("qenex_branding: de-branded %s %s", rec._name, xmlid)
