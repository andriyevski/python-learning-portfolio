# import json
#
# username = input("What is your name? ")
#
# filename = 'username.json'
# with open(filename, 'w', encoding = 'utf-8') as f:
#     json.dump(username, f)
#     print(f"We'll remember you when you come back, {username}!")
import json

filename = 'username.json'
try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename, 'w', encoding = 'utf-8') as f:
        json.dump(username, f)
        print(f"We'll remember you when you come back, {username}!")
else:
    print(f"Welcome back, {username}!")
