# import json
#
# username = input("What is your name? ")
#
# filename = 'username.json'
# with open(filename, 'w', encoding = 'utf-8') as f:
#     json.dump(username, f)
#     print(f"We'll remember you when you come back, {username}!")


# import json
#
# filename = 'username.json'
# try:
#     with open(filename) as f:
#         username = json.load(f)
# except FileNotFoundError:
#     username = input("What is your name? ")
#     with open(filename, 'w', encoding = 'utf-8') as f:
#         json.dump(username, f)
#         print(f"We'll remember you when you come back, {username}!")
# else:
#     print(f"Welcome back, {username}!")

# import json
#
# def greet_user():
#     """ Greet the user by name """
#     filename = 'username.json'
#     try:
#         with open(filename) as f:
#             username = json.load(f)
#     except FileNotFoundError:
#         username = input("What is your name? ")
#         with open(filename, 'w', encoding = 'utf-8') as f:
#             json.dump(username, f)
#             print(f"We'll remember you when you come back, {username}!")
#     else:
#         print(f"Welcome back, {username}!")
#
# greet_user()

import json

def get_stored_username():
    """ Take saved name a user if they created """
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_user():
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
        username = get_stored_username()
        if username:
            print(f"Welcome back, {username}!")
        else:
            username = get_new_user()
            print(f"We'll remember you when you come back, {username}!")



greet_user()
