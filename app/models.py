from . import db


class Properties(db.Model):
    __tablename__ = 'user_properties'

    property_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(80))
    num_bedrooms = db.Column(db.Integer)
    num_bathrooms = db.Column(db.Integer)
    location = db.Column(db.String(255))
    price = db.Column(db.String)
    property_type = db.Column(db.String(255))
    description = db.Column(db.String(255))
    property_photo = db.Column(db.String(255))

    def __init__(self, title, description, num_bedrooms, num_bathrooms, price, property_type, location, property_photo):
        self.title = title
        self.num_bedrooms = num_bedrooms
        self.num_bathrooms = num_bathrooms
        self.location = location
        self.price = price
        self. property_type = property_type
        self.description = description
        self.property_photo = property_photo
        