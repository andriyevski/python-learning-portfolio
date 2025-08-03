# The following code iterates through the list of
# named cars and searches for the value 'bmw'.
# For all elements containing the value 'bmw',
# the value is displayed in uppercase
# If = True or False
cars = ['audi','bmw','subaru','toyota']

for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

## Code ## :
# Audi
# BMW
# Subaru
# Toyota

# Bool check
car = 'BMW'
print(f'\ncar == {car} : {car =='BMW'}')
## Code ## : car == BMW : True

# Bool working different
print(f"\ncar == 'bmw' : {car == 'bmw'}")
## Code ## : car == 'bmw' : False

# Bool with methods work
car = 'Audi'
print(f"\ncar.lower() == 'audi': {car.lower() == 'audi'}")
## Code ## : car.lower() == 'audi': True
