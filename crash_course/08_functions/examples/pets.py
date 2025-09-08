# Position parametr must be first !
def describe_pet(pet_name, animal_type = 'dog'):
    """Выводит информацию о животном."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.\n")

# First argument can be write without parametr!
# Second argument is automatic set in function!
describe_pet('harry', animal_type = 'hamster')
describe_pet('Trump')
