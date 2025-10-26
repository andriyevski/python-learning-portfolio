import json

numbers = [2,3,4,7,11,23]

# Write in json in file
filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)


# read from file in str type
with open(filename, encoding = 'utf-8') as f:
    result = f.readline()
    print(type(result))
    print(result)

# read from file in write type
with open(filename, encoding = 'utf-8') as f:
    data = json.load(f)
    print(type(data))
    print(data)
