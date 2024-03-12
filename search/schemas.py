from flask_marshmallow import Marshmallow

marsh = Marshmallow()

class RestaurantSchema(marsh.Schema):
    name = marsh.String(dump_only=True)
    distance = marsh.Integer(dump_only=True)
    price = marsh.Integer(dump_only=True)
    customer_rating = marsh.Integer(dump_only=True)
    cuisine = marsh.String(dump_only=True)
    cuisine_id = marsh.Integer(dump_only=True)