from . import db, ma


class Taxon(db.Model):
    # See https://tools.gbif.org/dwca-validator/extension.do?id=dwc:Taxon#Taxon
    taxonID = db.Column(db.String(100))
    scientificName = db.Column(db.String(100))


class TaxonSchema(ma.ModelSchema):
    class Meta:
        model = Taxon
