# Just first three cars in list
cars = ['bmw','lexus','ford','audi','volvo']
print("The irst three items in the list are:")
for car in cars[:3]:
    print(car)

# Cars in middle list
print("Three items from the middle of the list are:")
for car in cars[2:3]:
    print(car)

# last three cars in list
print("The last three items in the list are:")
for car in cars[-3:]:
    print(car)
