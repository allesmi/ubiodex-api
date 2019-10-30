from . import db, ma

class Rank(object):
	name = db.Column(db.String(100))

	def __repr__self(self):
		return f'{self.__name__} "{self.name}"'

class Kingdom(Rank, db.Model):
	kingdom_id = db.Column(db.Integer, primary_key = True)

class KingdomSchema(ma.ModelSchema):
	class Meta:
		model = Kingdom

class Phylum(Rank, db.Model):
	phylum_id = db.Column(db.Integer, primary_key = True)

class PhylumSchema(ma.ModelSchema):
	class Meta:
		model = Phylum

class Class(Rank, db.Model):
	class_id = db.Column(db.Integer, primary_key = True)

class ClassSchema(ma.ModelSchema):
	class Meta:
		model = Class

class Order(Rank, db.Model):
	order_id = db.Column(db.Integer, primary_key = True)

class OrderSchema(ma.ModelSchema):
	class Meta:
		model = Order

class Family(Rank, db.Model):
	family_id = db.Column(db.Integer, primary_key = True)

class FamilySchema(ma.ModelSchema):
	class Meta:
		model = Family
