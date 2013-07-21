APP_NAME = 'barduino'
TAG = '0.0.1'

DEBUG = False
DEBUG_SQL = False

DEV = False

LOGGER_NAME = APP_NAME
LOG_ENABLE = True
LOG_FORMAT = '[%(process)d] %(levelname)s %(message)s [in %(pathname)s:%(lineno)d]'

DATABASE_URL = 'sqlite:///appdb.sqlite'

FACEBOOK_APP_ID = '387916474643695'
FACEBOOK_APP_SECRET = '6b62f2179f9fb7b6a420dea515ee74ea'

DISABLE_HTTP_ACCEPT_CHECK = False


TUBI = [(0, 'Gin'),
        (1, 'Vodka'), 
        (2, 'Martini Rosso'),
        (3, 'Aperol'),
        (4, 'Lemon Soda'),
        (5, 'Acqua Tonica'),
        (6, 'Red-bull')]
DRINKS = [('Vodka-Lemon', [0, .4, 0, 0, .6, 0, 0]),
          ('Gin-Lemon', [.35, 0, 0, 0, .65, 0, 0])]

try:
    from local_config import *
except ImportError:
    pass

try:
    from prod_config import *
except ImportError:
    pass
