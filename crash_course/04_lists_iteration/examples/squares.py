## Make range with task squares
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)

print(squares)
## Code ## : [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

## Example with another goal
numbers = []
for value in range(1,100):
    number = value **2
    numbers.append(number)

print(numbers)

# Or you can use analog, more clear code
numbers = []
for value in range(1,100):
    numbers.append(value**2)

print(numbers)

# But later we learn more effective pythonic list comprehension
squares = [value ** 2 for value in range(1,11)]
print(squares)
## Code ## : [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
