# Homework from file tasks/peoples.md
## Task ## : 6.7
# Peoples
from typing import Dict, Any


Peoples_Dict = Dict[str,Any]

class Person:
    def __init__(self,first_name: str,last_name: str,age: int,city: str ):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city


    def get_peoples(self) -> Peoples_Dict:
        """List with all users in dict"""
        return  {
            'first_name':self.first_name,
            'last_name':self.last_name,
            'age':self.age,
            'city':self.city,
        }

    def print_info(self) -> None:
        print(f"First name: {self.first_name}\n")
        print(f"Last name: {self.last_name}\n")
        print(f"Age: {self.age}\n")
        print(f"City: {self.city}\n")


if __name__ == "__main__":
    person1 = Person('Georg','Granovsky',38, 'Chicago')
    person2 = Person('Harry','Potter',15, 'London')
    person3 = Person('Bilbo','Heggens',38, 'Liverpool')

    persons = [person1, person2, person3]

    for user in persons:
        user.print_info()
        print("-"*50)
