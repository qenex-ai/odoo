{
    'name': 'QENEX Branding — Point of Sale',
    'summary': 'Strip Odoo branding from POS receipts and customer display.',
    'version': '19.0.1.0.0',
    'author': 'QENEX Systems',
    'website': 'https://qenex.ai',
    'license': 'LGPL-3',
    'category': 'Customizations',
    'depends': ['qenex_branding', 'point_of_sale'],
    'assets': {
        'point_of_sale._assets_pos': [
            'qenex_branding_pos/static/src/xml/order_receipt.xml',
            'qenex_branding_pos/static/src/xml/customer_display.xml',
        ],
    },
    'auto_install': True,
}
