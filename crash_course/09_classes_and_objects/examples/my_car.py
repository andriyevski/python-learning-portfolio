from car import Car


# Import our class and use him for our work
my_new_car = Car("Bmw", "7-Series", 2001)
print(my_new_car.get_descriptive_name())

# We buy new car and check it
my_new_car.read_odometer()

# Change odometr in car
my_new_car.update_odometer(90)

# Now we watch if this changes is set
my_new_car.read_odometer()
