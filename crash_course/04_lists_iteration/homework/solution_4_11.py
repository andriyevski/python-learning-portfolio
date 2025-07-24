# HOMEWORK
# My pizza solution
#
pizzas = ['Paperoni','Cezar','Salami','Margherita','Hawaii']
pizzas.append("Quattro formaggi")
friend_pizzas = pizzas[:]
friend_pizzas.append("Norway")
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("My friend’s favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
