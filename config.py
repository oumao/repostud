class Config:

    DEBUG = False
    TESTING = False
    SQLACHEMY_TRACK_MODIFICATION = False

class DevConfig(Config):

    """ Development Configuration """"
    ENV = 'development'
    TESTING = False
    DEBUG = True


class ProdConfig(Config):

     """ Production Configuration """"

    ENV = 'production'



class TestConfig(Config):

     """ Testing Configuration """"

    ENV = 'testing'
    TESTING = True


app_config = {
    'development' : DevConfig,
    'production' : ProdConfig,
    'testing' : TestConfig
}