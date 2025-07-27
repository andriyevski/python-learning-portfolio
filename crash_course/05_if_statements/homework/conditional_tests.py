# Home task
user_car = 'bmw'
cars = ['audi','bmw','ford','lexus','mazda','Range Rover']

if user_car in cars:
    print(f"\n Yes we have {user_car} in our market !")
    print(f"\nYou want buy? {user_car}")
else:
    print(f"\nNo we dont have a {user_car} in our market!")
    print("\nMaybe you wanna buy this cars:")
    for car in cars:
        print(f"We have a new {car.title()}")
for car in cars:
    if len(car) > len(user_car):
        print(f"This {user_car} have less letter in name! Then in car: {car}")
    elif len(car) == len(user_car):
        print(f"Oh my god... Your car: {user_car} have the same letter like our car: {car}")
    else:
        print(f"This car: {user_car} have more letter in name! Then our car: {car}")
if user_car not in cars:
    cars.append(user_car)
    print(f"Now we add: {user_car} in list!")
else:
    for car in cars:
        print(f"Our market have : {car.lower()}")
