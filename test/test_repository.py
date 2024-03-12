from search.repository import RestaurantRepository, CuisineRepository


def test_restaurant_repository_import():
    # Arrange
    restaurant_repository = RestaurantRepository()

    # Act
    restaurants = restaurant_repository.restaurants

    # Assert
    assert len(restaurants) > 0  # Assuming there should be data in the CSV

def test_cuisine_repository_import():
    # Arrange
    cuisine_repository = CuisineRepository()

    # Act
    cuisines = cuisine_repository.cuisines

    # Assert
    assert len(cuisines) > 0  # Assuming there should be data in the CSV