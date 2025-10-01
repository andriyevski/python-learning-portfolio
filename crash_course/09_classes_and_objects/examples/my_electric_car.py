from electric_car import Car, ElectricCar

my_tesla = ElectricCar("Tesla" , "Model-Y", 2025)
print(my_tesla.get_descriptive_name())
my_tesla.battery.get_describe_battery()
my_tesla.battery.get_range()


my_bmw = Car('Bmw', 'i3', 2025)
print(my_bmw.get_descriptive_name())
