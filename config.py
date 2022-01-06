import os
class Config:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATION = False
    SUBMITTED_ASSIGNMENT = os.path.join(os.getcwd(), "repoapp/static/submitted_assignments")


class DevConfig(Config):
    """ Development Configuration """

    ENV = 'development'
    TESTING = True
    DEBUG = True


class ProdConfig(Config):
    """ Production Configuration """

    ENV = 'production'


class TestConfig(Config):
    """ Testing Configuration """

    ENV = 'testing'
    TESTING = True


app_config = {
    'development': DevConfig,
    'production': ProdConfig,
    'testing': TestConfig
}


