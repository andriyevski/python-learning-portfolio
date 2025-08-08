# Homework from file tasks/home_pets.md
## Task ## : 6.8
# 6_8_home_pets
from typing import Dict,Any

Pets_Dict = Dict[str,Any]


class Pets:
    def __init__(self, name: str, pet_type: str, age: int, sex: int, vaccinated: int):
        self.name = name
        self.pet_type = pet_type
        self.age = age

        # Converstation to str
        if sex == 0:
            self.sex = "male"
        else:
            self.sex = "female"

        if vaccinated == 0:
            self.vaccinated = "No"
        else:
            self.vaccinated = "Yes"

    def get_pets(self) -> Pets_Dict:
        """Make Dict about Pets"""
        return {
            'name' : self.name,
            'pet_type' : self.pet_type,
            'age' : self.age,
            'sex' : self.sex,
            'vaccinated' : self.vaccinated
        }

    def print_pets(self) -> None:
        """Print info about pets!"""
        print(f"Name: {self.name}\n")
        print(f"Type: {self.pet_type}\n")
        print(f"Age: {self.age}\n")
        print(f"sex: {self.sex}\n")
        print(f"Vaccinated: {self.vaccinated}\n")
        print("-"*10)

def test_pets():
    cat = Pets('mew', 'real cat', 1, 1, 1)
    expected = {
        'name': 'mew',
        'pet_type': 'real cat',
        'age': 1,
        'sex': 'female',
        'vaccinated': 'Yes'
    }
    assert cat.get_pets() == expected


if __name__ == "__main__":
    """Create any pets, no limit->
            name: What is name pet? -> [str]
            pet_type: type of cat -> [str]
            age: age of cat -> [int]
            sex: male: 0, female: 1 ->[int]
            vaccinated: 'No': 0, 'Yes : 1'
    """
    # Test if all work!
    test_pets()
    
    cat1 = Pets('Mishka','British Cat',12,0,0)
    cat2 = Pets('Monika','Canadian Cat', 2,1,1)
    cat3 = Pets('Roxana', 'Carpatian cat', 3,1,0)

    pets = [cat1, cat2, cat3]

    # Show info about all base with pets
    for cat in pets:
        cat.print_pets()
