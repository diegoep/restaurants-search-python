from search import util
from search.index import distance_index, rating_index, price_index, restaurant_index, cuisine_index
from search.repository import restaurant_repository


class RestaurantService:
    def __init__(self, restaurant_repository):
        self.restaurant_repository = restaurant_repository

    def search(self, query):
        results = []

        if query.distance:
            results.append(distance_index.get_items_less_or_equals_than(int(query.distance)))

        if query.rating:
            results.append(rating_index.get_items_greater_or_equals_than(int(query.rating)))

        if query.price:
            results.append(price_index.get_items_less_or_equals_than(int(query.price)))

        if query.name:
            restaurants_by_name = restaurant_index.search(query.name)
            results.append(restaurants_by_name)

        if query.cuisine:
            cuisine_search_result = cuisine_index.search(query.cuisine)
            result = []
            for cuisine in cuisine_search_result:
                restaurants_with_cuisine = restaurant_repository.find_by_cuisine(cuisine.id)
                for restaurant in restaurants_with_cuisine:
                    result.append(restaurant)
            results.append(result)

        if not query.distance and not query.rating and not query.price and not query.name and not query.cuisine:
            results.append(restaurant_repository.find_all())

        return util.find_intersection(results)


restaurant_service = RestaurantService(restaurant_repository)
