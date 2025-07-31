# Solution 5.3
# Color N1

# Condition True
alien_color = 'green'

if alien_color == 'green':
    points = 5
print(f"You take right now {points} points!")

# Condition False
points = 0
if alien_color != 'green':
    points = 5
print(f"You take right now {points} points!")


# Solution 5.4
# Color N2
alien_color = 'green'

if alien_color == 'green':
    points = 5
else:
    points = 10
print(f"Now you have 'True' and take {points} points!")

if alien_color != 'green':
    points = 5
else:
    points = 10
print(f"Now you have 'False' take {points} points!")


# Solution 5.5
# Color N3
alien_color = 'red'

if alien_color == 'yellow':
    points = 10
elif alien_color == 'red':
    points = 15
else:
    points = 5
print(f"Now you take {points} points!")


# Solution 5.6
# Color N4
age = 10

if age < 2:
    result_age = "baby"
elif age < 4:
    result_age = "Kid"
elif age < 13:
    result_age = "Child"
elif age < 20:
    result_age = "Teenager"
elif age < 65:
    result_age = "Adult"
else:
    result_age = "An elderly man"

print(f"You are {result_age} in this time of moment!")

# Solution 5.7
# Color N5
fruits = ['apple','banana','orange','lime','watermelon']

favorite_fruits = fruits[2:]
favorite_fruits.append(fruits[0])

if 'apple' in favorite_fruits:
    fruit = 'apple'
    print(f" You really like {fruit}!")
if 'banana' in favorite_fruits:
    fruit = 'banana'
    print(f" You really like {fruit}!")
if 'orange' in favorite_fruits:
    fruit = 'orange'
    print(f" You really like {fruit}!")
if 'lime' in favorite_fruits:
    fruit = 'lime'
    print(f" You really like {fruit}!")
if 'watermelon' in favorite_fruits:
    fruit = 'watermelon'
    print(f" You really like {fruit}!")
