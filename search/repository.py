from search import util
from search.model import Restaurant, Cuisine


class RestaurantRepository:
    def __init__(self):
        self.__import_restaurants()

    def find_all(self):
        return self.restaurants

    def find_by_cuisine(self, cuisine_id):
        return list(filter(lambda r: r.cuisine_id == cuisine_id, self.restaurants))

    def __import_restaurants(self):
        rest_dics = util.read_csv('data/restaurants.csv')
        self.restaurants = [Restaurant(**rest) for rest in rest_dics]


class CuisineRepository:
    def __init__(self):
        self.__import_cuisines()

    def find_all(self):
        return self.cuisines

    def __import_cuisines(self):
        cuisine_dicts = util.read_csv('data/cuisines.csv')
        self.cuisines = [Cuisine(**cuisine) for cuisine in cuisine_dicts]


restaurant_repository = RestaurantRepository()
cuisine_repository = CuisineRepository()
