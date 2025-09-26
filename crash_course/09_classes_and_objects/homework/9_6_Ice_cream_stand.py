# Homework from file tasks/9_6_Ice_cream_stand.md
## Task ## : 9.6
# 9_6_Ice_cream_stand
from typing import List

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


class IceCreamStand(Restaurant):
    """ Like restourant class """
    def __init__(self, restaurant_name: str, cuisine_type: str, flavors: List[str], pcs: int) -> None:
        super().__init__(restaurant_name,cuisine_type)
        """
        flavors:
        - mint
        - coconut
        - white
        pcs:
        -1 pcs ice cream
        -2 pcs ice cream
        """
        self.flavors = flavors
        self.pcs = pcs

        print(f"Welcome in '{self.restaurant_name.title()}' ice cream stand!")

    def show_my_ice_cream(self):
        """ Print the pick ice cream """
        print(f"Thank you for pick Ice Cream with:")
        for flavour in self.flavors:
            print(f"- {flavour.title()}")
        print(f"And you buy {self.pcs} pcs!")


my_stand = IceCreamStand('Coldy','Open', ['Watermelon','chocolate','mint'], 2)
my_stand.show_my_ice_cream()
my_stand.describe_restaurant()
