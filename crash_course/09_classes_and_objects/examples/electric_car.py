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


class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        # self.battery_size = 75
        self.battery = Battery()
    # def get_describe_battery(self):
    #     """ Init battery power! """
    #     print(f"This car has a {self.battery_size}-kwh batery")

    def fill_gas_tank(self):
        """ Electro car doesn't have a gas tank """
        print("This car doesn't need a gas tank!")

class Battery():
    """ Simple model of Battery car """
    def __init__(self, battery_size = 75):
        self.battery_size = battery_size

    def get_describe_battery(self):
        print(f"This car has a {self.battery_size}-kwh batery")


my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23)
my_new_car.increment_odometer(140_000)




my_electro_car = ElectricCar('Tesla', 'Model Y', 2023)
print(my_electro_car.get_descriptive_name())
my_electro_car.battery = Battery(battery_size=125)
my_electro_car.battery.get_describe_battery()
