# List Sorting:
# Often, lists are created in an unpredictable order because user input isn't always controlled.
# While this is sometimes unavoidable, data frequently needs to be displayed in a specific order.
# Python offers several ways to sort a list depending on the situation:
# 1. Permanent Sorting with the sort() method:
#    This method permanently changes the order of elements in a list to alphabetical.
#    Example: A list of cars being sorted alphabetically.
cars = ['bmw','audi','toyota','subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

# Temporary Sorting with the sorted() function:
# To preserve the original order of a list while presenting its elements in a sorted order temporarily,
# you can use the sorted() function. This function displays the list in a specific order but
# does not change the actual order of elements in the original list.
# Let's try applying this function to the car list.
cars = ['bmw','audi','toyota','subaru']
print('\nHere is original list:')
print(cars)

print('\nHere is sorted list:')
print(sorted(cars))

print('\nHere is original list agan:')
print(cars)

## Use reverse()
#
cars.reverse()
print(cars)

## Use len()
#
print(len(cars))
