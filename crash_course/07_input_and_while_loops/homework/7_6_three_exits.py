# Homework from file tasks/7_6_three_exits.md
## Task ## : 7.6
# 7_6_three_exits

toppings = set()
active = True  # Управление циклом через переменную

while active:  # Выход через условие в while
    topping = input("\nEnter the best topping what do you want :")

    if topping == "quit":
        print("Thanks for adding! Good bye!")
        break  # Выход через break

    if topping == "stop":
        print("Session ended via 'stop' command.")
        active = False  # Управление циклом через переменную
        continue

    if not topping.strip():
        print("You did not write anything, error!")
        continue

    if topping not in toppings:
        toppings.add(topping)
        print("You added: " + topping + " to the set!")
    else:
        print("You already picked: " + topping)

    print("Current toppings:", toppings)
