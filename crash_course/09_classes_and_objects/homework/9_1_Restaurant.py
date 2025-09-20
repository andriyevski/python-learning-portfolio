# Homework from file tasks/9_1_Restaurant.md
## Task ## : 9.1
# 9_1_Restaurant
class Restaurant():
    """
    to people info If restaurant open or not
    """
    def __init__(self, restaurant_name, cuisine_type):
        """ Init class """
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """ print atrebutes """
        print(f"The restaurant {self.restaurant_name} type is {self.cuisine_type} right now!")

    def open_restaurant(self):
        """ Message if restaurant open """
        print(f"Restaurant restaurant {self.restaurant_name} is open!")

restaurant = Restaurant("Royal","Turkey")
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant2 = Restaurant("Pikaboo","Japan")
restaurant2.describe_restaurant()
restaurant2.open_restaurant()
