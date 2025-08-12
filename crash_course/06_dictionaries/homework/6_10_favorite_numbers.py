# Homework from file tasks/favorite_numbers.md
## Task ## : 6.10
# 6_10_ Favorite Numbers
names = ['mike','zlotan','helga','artur','regina']
numbers = [[5,6,7],[11,12,13],[7,14,21],[44,88,256,666],[777,999,1024,888]]

for i in range(len(names)):
    print(f"\n{names[i]}'s favorite numbers are:")
    for number in numbers[i]:
        print(f" - {number}")

print("-"*20)
print("Or use like this, more Pythonic!")
print("-"*30)
# or use this

for name, fav_numbers in zip(names, numbers):
    print(f"\n{name}'s favorite numbers are:")
    for number in fav_numbers:
        print(f" - {number}")
