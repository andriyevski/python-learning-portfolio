# My list with favorite food and my friends
my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]
# if we use friend_foods = my_foods
# we just make a link to my_foods, not a new list

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite fods are:")
print(friend_foods)
