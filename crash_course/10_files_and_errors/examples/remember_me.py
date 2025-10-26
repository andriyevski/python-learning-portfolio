import json

username = input("What is your name? ")

filename = 'username.json'
with open(filename, 'w', encoding = 'utf-8') as f:
    json.dump(username, f)
    print(f"We'll remember you when you come back, {username}!")
