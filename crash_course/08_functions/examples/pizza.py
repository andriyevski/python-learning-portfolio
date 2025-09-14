def make_pizza(size, *toppings):
    """
    Print list of all picked toppings!
    - *toppings -> Python create a empty list with type (Tuple)
    -- *args -> is default name of positional arguments with an arbitrary set of arguments
    --------------------
    - **toppings -> Python create a empty list with type (Dict) save like >> key:value
    -- **kwargs -> is default arbitrary set of named sets
    """
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(30,'papperoni')
make_pizza(60,'mashrooms', 'green pappers', 'extra cheese')
