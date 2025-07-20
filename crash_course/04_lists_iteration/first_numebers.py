## Use range() for make a list with numbers!
for value in range(1,5):
    print(value)
# We take only 1,2,3,4. iterator come to 5 but do not print
# fix it
for value in range(1,6):
    print(value)
## Code ## : now we can take 1,2,3,4,5
for value in range(6):
    print(value)
## Code ## : 0,1,2,3,4,5 but 6 is not printed remember

# Generate list
numbers = list(range(1,6))
print(numbers)
## Code ## : [1,2,3,4,5]
