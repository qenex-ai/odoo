{
    'name': 'QENEX Branding — Attendance Kiosk',
    'summary': 'Strip Odoo branding from the attendance public kiosk.',
    'version': '19.0.1.0.0',
    'author': 'QENEX Systems',
    'website': 'https://qenex.ai',
    'license': 'LGPL-3',
    'category': 'Customizations',
    'depends': ['qenex_branding', 'hr_attendance'],
    'assets': {
        'hr_attendance.assets_public_attendance': [
            'qenex_branding_hr_attendance/static/src/xml/public_kiosk_app.xml',
        ],
    },
    'auto_install': True,
}
