{
    # App Information
    'name': 'Chatter Message Clear',
    'version': '17.0.1.0.0',
    'license': 'LGPL-3',
    'summary': 'Clear all chatter messages from a record with confirmation (Delete chatter message, chatter Message Clear clear chatter, remove log note, delete message from chatter, Odoo chatter delete, chatter message delete, delete chatter history, remove chatter message, delete log note, clear record discussion, delete record messages)',
    'description': """
    Chatter Message Clear
    =====================
    
    Adds a clear action in the backend chatter to delete all messages from the
    current record after an explicit confirmation.
    """,
    'category': 'Productivity',

    # Author
    'author': 'Techno Stellar',
    'maintainer': 'Techno Stellar',

    # dependencies
    'depends': ['mail', 'web'],

    # Views & Data
    'data': [
        'security/security.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'chatter_message_clear_tspl/static/src/js/chatter_clear_patch.js',
            'chatter_message_clear_tspl/static/src/xml/chatter_clear_button.xml',
        ],
    },

    # Technical
    'images': ['static/description/banner_v17.png',],
    'installable': True,
    'application': False,
    'auto_install': False,

    # Pricing
    'price': 0.0,
    'currency': 'EUR',
}
