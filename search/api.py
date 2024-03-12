import json

from flask import Blueprint, request, jsonify

from search.schemas import RestaurantSchema
from search.services import restaurant_service

# Create a Blueprint object for API routes
api = Blueprint('api', __name__)


# Define your API routes using the Blueprint object
@api.route('/')
def index():
    query = RestaurantQuery(request.args.get('name'),
                            request.args.get('rating'),
                            request.args.get('distance'),
                            request.args.get('price'),
                            request.args.get('cuisine'))
    result = restaurant_service.search(query)
    return restaurant_schema.jsonify(result, many=True)


class RestaurantQuery:
    def __init__(self, name, rating, distance, price, cuisine):
        self.name = name if name else ''
        self.rating = rating if rating else ''
        self.distance = distance if distance else ''
        self.price = price if price else ''
        self.cuisine = cuisine if cuisine else ''

    def __str__(self):
        return "Name: " + self.name + " Rating: " + self.rating + " Distance: " + self.distance + " Price: " + self.price + " Cuisine: " + self.cuisine


restaurant_schema = RestaurantSchema()