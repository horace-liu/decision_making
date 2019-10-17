from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 1.00,
    'participation_fee': 0.00,
    'doc': "",
}

SESSION_CONFIGS = [
    #{
    #    'name': 'public_goods',
    #    'display_name': "Public Goods",
    #    'num_demo_participants': 3,
    #    'app_sequence': ['public_goods', 'payment_info'],
    #},
    {
       'name': 'GXX',
       'display_name': "GXX's Splendid Experiment ",
       'num_demo_participants': 6,
       'app_sequence': ['coverstory', 'StaticVo', 'StaticTom', 'Dynamic_init', 'Dynamic_self', 'Theend']
    },
]


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = []

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '!o8lkg!nuoth*^%(ujm)4th2w@rsni!cm@+(x=je%_e(6#6&3h'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
