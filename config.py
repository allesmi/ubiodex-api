import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	CONFIG_NAME = 'Default'
	DEBUG = False
	TESTING = False
	CSRF_ENABLED = True
	SECRET_KEY = 'Dev'
	
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite://' + os.path.join(basedir, 'app.db'))
	SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
	CONFIG_NAME = 'Production'
	DEBUG = False

class DevelopmentConfig(Config):
	CONFIG_NAME = 'Development'
	ENV = 'development'
	DEVELOPMENT = True
	DEBUG = True
