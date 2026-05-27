# patches/

Reserved. No core patches are required at v19.0 — every user-visible
Odoo surface in scope is reachable through QWeb inheritance, OWL
`t-inherit`, JS `patch()` from `@web/core/utils/patch`, controller
subclassing, model `_inherit`, `ir.config_parameter`, SCSS asset
bundles, or `mail.template` data record overrides.

If a future Odoo version moves a brand surface beyond inheritance,
drop the diff here as `NN-short-name.patch` with a header comment
explaining why an override wasn't possible.
