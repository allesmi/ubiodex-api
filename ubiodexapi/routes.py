from flask_restful import Resource, Api

def setup_api_routes(app):
	API_PREFIX = '/api'
	
	api = Api(app)

	class Test(Resource):
		def get(self):
			return { 'hello': 'world' }

	api.add_resource(Test, f'{API_PREFIX}/')

def setup_routes(app):

	@app.route('/')
	def hello():
		return 'Hello World!'

	setup_api_routes(app)