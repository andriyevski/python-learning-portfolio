# Homework from file tasks/9_2_Three_restaurants.md
## Task ## : 9.2
# 9_2_Three_restaurants
class Restaurant():
    """
    to people info If restaurant open or not
    """
    def __init__(self, restaurant_name: str, cuisine_type: str) -> None:
        """ Init class """
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """ print atrebutes """
        print(f"The restaurant {self.restaurant_name} type is {self.cuisine_type} right now!")

    def open_restaurant(self):
        """ Message if restaurant open """
        print(f"Restaurant restaurant {self.restaurant_name} is open!")


restaurant_1 = Restaurant('Yoki', 'japan')
restaurant_2 = Restaurant('Burger King', 'Usa')
restaurant_3 = Restaurant('Spaghettini', 'Italia')


restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()
