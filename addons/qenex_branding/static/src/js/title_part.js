/** Seed the title service with a default "QENEX" part.
 *
 *  The empty-state fallback string in @web/core/browser/title_service is
 *  `|| "Odoo"`. We don't patch that closure; instead we register a
 *  service that runs after `title` and sets a baseline part, so the
 *  join always produces "<page> - QENEX" (or just "QENEX" with no parts).
 */
import { registry } from "@web/core/registry";

const qenexTitleService = {
    dependencies: ["title"],
    start(env, { title }) {
        title.setParts({ zopenerp: "QENEX" });
    },
};

registry.category("services").add("qenex_branding.title", qenexTitleService);
