# Homework from file tasks/7_9_without_pastrami.md
## Task ## : 7.9
# 7_9_without_pastrami
sandwich_orders = ['Pepperoni','pastrami','Fish','paStrami','Meat', 'Cheese','pastrami']
clear_sandwich_orders = []
active = True

print("Pastrami no more in sandwich_orders!")
count = 0

while active:
    if count < len(sandwich_orders):
        if 'pastrami' not in sandwich_orders[count].lower():
            clear_sandwich_orders.append(sandwich_orders[count])
            count += 1
        else:
            count += 1
    else:
        break

for sandwich in clear_sandwich_orders:
    if 'pastrami' in sandwich:
        print("Yeah 'pastrami' in sandwich_orders!")
    else:
        print("Nope, 'pastrami' all clear!")
