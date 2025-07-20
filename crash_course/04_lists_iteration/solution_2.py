# Task_1
# Use only for to task, from 1 to 20 include
for value in range(1,21):
    print(value)

# Task_2
# greated list with numbers from 1 to 1 000 000
numbers = [value for value in range(1,1_000_001)]

# Task_3
# Now we need see all numbers in list in cycle
for value in numbers:
    print(value)

print(min(numbers))
print(max(numbers))
print(sum(numbers))

# Task_4
# odd numbers
numbers = [value for value in range(1,21,2)]
for number in numbers:
    print(number)

# Task_5
# Non odd numbers
numbers = [value for value in range(3,30,3)]
for number in numbers:
    print(number)

# Task_6
# Task сubes
numbers = [value **3 for value in range(1,11)]
for number in numbers:
    print(number)

# Task_7
# make a list with list of all cubes in numbers
cube_lists = [value**3 for value in range(1,11)]
