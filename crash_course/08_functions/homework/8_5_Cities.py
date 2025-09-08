# Homework from file tasks/8_5_Cities.md
## Task ## : 8.5
# 8_5_Cities

def describe_city(city: str = "Lviv", country: str = "Ukraine") -> None:
    """
    Parameter:
    - city (str): Enter the name of 8_5_Cities
    and we can continue the country of this sitie!
    """
    if not city.strip() or not country.strip():
        print("\nError: City or country name is missing.")
    else:
        print(f"\n{city.title()} is in {country.title()}")


describe_city("Lviv")
describe_city("New York","USA")
describe_city("Berlin","Germany")
describe_city("toronto","canada")
describe_city("","")
describe_city("Moscow")
describe_city(country="Spain")
describe_city(city="Sozopol")
describe_city()
describe_city(" ")
