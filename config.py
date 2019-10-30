import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	CONFIG_NAME = 'Default'
	DEBUG = False
	TESTING = False
	CSRF_ENABLED = True
	SECRET_KEY = 'Dev'

class ProductionConfig(Config):
	CONFIG_NAME = 'Production'
	DEBUG = False

class DevelopmentConfig(Config):
	CONFIG_NAME = 'Development'
	ENV = 'development'
	DEVELOPMENT = True
	DEBUG = True
