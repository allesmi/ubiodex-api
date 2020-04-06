from flask import current_app as app
from flask_restful import Resource, Api

from .models import (
    Taxon, TaxonSchema
)

API_PREFIX = '/api'

api = Api(app)


class TaxonResource(Resource):
    def get(self):
        l = Taxon.query.all()

        schema = TaxonSchema()
        return schema.dump(l, many=True)


class Test(Resource):
    def get(self):
        return {'hello': 'world'}


api.add_resource(TaxonResource, f'{API_PREFIX}/taxon')


@app.route('/')
def hello():
    return 'Hello World!'
