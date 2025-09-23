# Homework from file tasks/9_4_Visitors.md
## Task ## : 9.4
# 9_4_Visitors
class Restaurant():
    """
    to people info If restaurant open or not
    """
    def __init__(self, restaurant_name, cuisine_type):
        """ Init class """
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.served_count = 0

    def describe_restaurant(self):
        """ print atrebutes """
        print(f"The restaurant {self.restaurant_name} type is {self.cuisine_type} right now!")

    def open_restaurant(self):
        """ Message if restaurant open """
        print(f"Restaurant restaurant {self.restaurant_name} is open!")

    def set_number_served(self, numb_peoples):
        """ Set count of served tables or peoples """
        self.served_count += numb_peoples
        print(f"Right now served {self.served_count} peoples.")

    def increment_number_served(self, set_served_peoples):
        """ set served peoples in ones the day """
        total_reserved = self.served_count+set_served_peoples
        print(f"Today served {total_reserved} in the one day!")

tokyo = Restaurant('Tokyo', 'Japan')
tokyo.describe_restaurant()
tokyo.set_number_served(5)
tokyo.set_number_served(5)
tokyo.increment_number_served(10)
