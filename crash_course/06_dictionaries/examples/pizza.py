pizza = {
    'crust':'thick',
    'toppings':['mashrooms','extra cheese'],
    }

print(f"You order a {pizza['crust']} -- crust pizza"
        "with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t + {topping}")
