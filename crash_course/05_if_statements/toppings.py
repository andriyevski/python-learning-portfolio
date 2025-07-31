# if-else explain
requested_toppings = ['mashrooms','green peppers','extra cheese']

if 'mashrooms' in requested_toppings:
    print(f"Adding mashrooms.")
if 'paperoni' in requested_toppings:
    print(f"Adding paperoni.")
if 'extra cheese' in requested_toppings:
    print(f"Adding extra cheese.")
else:
    print("I dont have ingradient!")
print(f"Finished making your pizza!")

# or use this # OPTIMIZE: code
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print(f"Sorry, we are out of green right now.")
    else:
        print(f"Adding {requested_topping}.")
print(f"Finished making your pizza!")

# New task

requested_toppings = []
if requested_toppings:
    if requested_topping == 'green peppers':
        print(f"Sorry, we are out of green right now.")
    else:
        print(f"Adding {requested_topping}.")
print(f"Are you sure you want a plain pizza?")
