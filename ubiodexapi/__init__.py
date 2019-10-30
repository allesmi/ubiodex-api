#!/usr/bin/env python3

import os

from flask import Flask

def create_app(test_config=None):
	# create and configure the app
	app = Flask(__name__, instance_relative_config=True)

	# Configuration
	if test_config is None:
		# load the instance config, if it exists, when not testing
		app.config.from_object(os.environ.get('APP_SETTINGS', 'config.Config'))
	else:
		# load the test config if passed in
		app.config.from_mapping(test_config)
	print(f'Using configuration: {app.config["CONFIG_NAME"]}')

	# ensure the instance folder exists
	try:
		os.makedirs(app.instance_path)
	except OSError:
		pass

	# a simple page that says hello
	@app.route('/')
	def hello():
		return 'Hello World!'

	return app
