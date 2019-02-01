from config import get_env

class EnvConfig(object):
    """Parent configurations class."""
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = get_env('SECRET')

class DevelopmentEnv(EnvConfig):
    """Configuration for Development."""
    DEBUG = True

class TestingEnv(EnvConfig):
    """Configuration for Testing, with a separate test database."""
    TESTING = True
    DEBUG = True

class StagingEnv(EnvConfig):
    """Configuration for Staging."""
    DEBUG = True

class ProductionEnv(EnvConfig):
    """Configuration for Production."""
    DEBUG = False
    TESTING = False

app_env = {
    'development': DevelopmentEnv,
    'testing': TestingEnv,
    'Staging': StagingEnv,
    'production': ProductionEnv,
}
