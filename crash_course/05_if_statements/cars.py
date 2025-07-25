# The following code iterates through the list of
# named cars and searches for the value 'bmw'.
# For all elements containing the value 'bmw',
# the value is displayed in uppercase
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
