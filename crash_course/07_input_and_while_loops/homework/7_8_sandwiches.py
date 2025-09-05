# Homework from file tasks/7_8_sandwiches.md
## Task ## : 7.8
# 7_8_sandwiches

# Список заказов на сэндвичи
sandwich_orders = ['Pepperoni', 'Fish', 'Meat', 'Cheese']
finished_sandwiches = []

# Перебор заказов и создание сэндвичей
for sandwich in sandwich_orders:
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

# Вывод списка изготовленных сэндвичей
print("\nAll sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich} sandwich")
