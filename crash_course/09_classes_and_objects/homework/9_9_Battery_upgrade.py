# Homework from file tasks/9_9_Battery_upgrade.md
## Task ## : 9.9
# 9_9_Battery_upgrade
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        return f"{self.year} {self.make} {self.model}"


class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        if self.battery_size != 100:
            self.battery_size = 100


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


# Create an electric car instance and test battery upgrade
my_tesla = ElectricCar('Tesla', 'Model S', 2020)

print("Before upgrade:")
my_tesla.battery.get_range()

my_tesla.battery.upgrade_battery()

print("After upgrade:")
my_tesla.battery.get_range()
