from flask import current_app as app
from flask_restful import Resource, Api

from .models import (
	Kingdom, KingdomSchema,
	Phylum, PhylumSchema,
	Class, ClassSchema,
	Order, OrderSchema,
	Family, FamilySchema
)

API_PREFIX = '/api'

api = Api(app)

class KingdomResource(Resource):
	def get(self):
		l = Kingdom.query.all()

		schema = KingdomSchema()
		return schema.dump(l, many=True)

class PhylumResource(Resource):
	def get(self):
		l = Phylum.query.all()

		schema = PhylumSchema()
		return schema.dump(l, many = True)

class ClassResource(Resource):
	def get(self):
		l = Class.query.all()

		schema = ClassSchema()
		return schema.dump(l, many = True)

class OrderResource(Resource):
	def get(self):
		l = Order.query.all()

		schema = OrderSchema()
		return schema.dump(l, many = True)

class FamilyResource(Resource):
	def get(self):
		l = Family.query.all()

		schema = FamilySchema()
		return schema.dump(l, many = True)

class Test(Resource):
	def get(self):
		return { 'hello': 'world' }

api.add_resource(KingdomResource, f'{API_PREFIX}/kingdom')
api.add_resource(PhylumResource, f'{API_PREFIX}/phylum')
api.add_resource(ClassResource, f'{API_PREFIX}/class')
api.add_resource(OrderResource, f'{API_PREFIX}/order')
api.add_resource(FamilyResource, f'{API_PREFIX}/family')

@app.route('/')
def hello():
	return 'Hello World!'
