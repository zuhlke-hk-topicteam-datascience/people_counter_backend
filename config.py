class Config(object):
    DEBUG = True
    DEVELOPMENT = True
    DB_HOST = 'localhost'

class ProductionConfig(Config):
    DEVELOPMENT = False
    DEBUG = False
    DB_HOST = 'my.production.database'