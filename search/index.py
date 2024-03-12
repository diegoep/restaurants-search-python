from search.data_structures import PrefixTrie
from search.repository import restaurant_repository, cuisine_repository


class NumberInvertedIndex:
    def __init__(self):
        self.inverted_index = dict()

    def add_data(self, key, data):
        if key not in self.inverted_index:
            self.inverted_index[key] = []
        self.inverted_index[key].append(data)

    def get_items_less_or_equals_than(self, max):
        from_index = [value for key, value in self.inverted_index.items() if key <= max]
        result = [item for sublist in from_index for item in sublist]
        return result

    def get_items_greater_or_equals_than(self, min):
        from_index = [value for key, value in self.inverted_index.items() if key >= min]
        result = [item for sublist in from_index for item in sublist]
        return result

    def get_item(self, key):
        return self.inverted_index[key]


class PartialStringInvertedIndex:
    def __init__(self):
        self.inverted_index = PrefixTrie()

    def add_data(self, word, data):
        # Perform string operations on the word
        word = word.strip().lower().translate(str.maketrans('', '', ' \t\n\r\f\v!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'))

        # Insert the modified word and data into the invertedIndex (PrefixTrie)
        self.inverted_index.insert(word, data)

    def search(self, word):
        return self.inverted_index.search(word)


price_index = NumberInvertedIndex()
rating_index = NumberInvertedIndex()
distance_index = NumberInvertedIndex()
restaurant_index = PartialStringInvertedIndex()
cuisine_index = PartialStringInvertedIndex()

for restaurant in restaurant_repository.find_all():
    price_index.add_data(int(restaurant.price), restaurant)
    rating_index.add_data(int(restaurant.customer_rating), restaurant)
    distance_index.add_data(int(restaurant.distance), restaurant)
    restaurant_index.add_data(restaurant.name, restaurant)

for cuisine in cuisine_repository.find_all():
    cuisine_index.add_data(cuisine.name, cuisine)

