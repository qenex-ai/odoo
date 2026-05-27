/** Patch the Dialog default title to "QENEX".
 *
 *  Odoo's @web/core/dialog/dialog ships `title: "Odoo"` as the
 *  fallback defaultProps. Reachable via Odoo's standard patch() helper,
 *  no source edit needed.
 */
import { Dialog } from "@web/core/dialog/dialog";
import { patch } from "@web/core/utils/patch";

patch(Dialog, {
    defaultProps: {
        ...Dialog.defaultProps,
        title: "QENEX",
    },
});
