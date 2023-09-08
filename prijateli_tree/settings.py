from os import environ


SESSION_CONFIGS = []

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    "real_world_currency_per_point": 1.00,
    "participation_fee": 0.00,
    "doc": "",
}

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

# ISO-639 code
LANGUAGE_CODE = "en, tr, sq, mk"

REAL_WORLD_CURRENCY_CODE = "DZD"
USE_POINTS = True

ADMIN_USERNAME = "admin"
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get("OTREE_ADMIN_PASSWORD")

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = "6643183821396"
