class Car():
    """
    Simple car model
    """

    def __init__(self, make, model, year):
        """ init atributes about auto """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """ return info """
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name.title()

    def read_odometer(self):
        """ Print how much car ride in miles """
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """ Set our value in odometr """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """ You can add miles to odometer """
        self.odometer_reading += miles


my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23)
my_new_car.increment_odometer(140_000)
my_new_car.read_odometer()
