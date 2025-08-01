# Solution 5.8
# Name: Hello Admin

users = ['admin','serhii','john','erik','eva','mike','steve']

for user in users:
    if user == 'admin':
        print(f"\nHello admin, would you like to see a status report?")
    else:
        print(f"\nHello {user}, thank you for logging in again")


# Solution 5.9
# Name: Without User
users.clear()
if users:
    pass
else:
    print(f"We need to ind some users!")


# Solution 5.10
# Name: Check name of users
current_users = ['aDmiN','serhii','john','erik','eva','mike','steve']
new_users = ['nate','hose','lola','pedro','rocky','admin','mikE']

for user in new_users:
    current_users_lower = [user.lower() for user in current_users]
    if user.lower() in current_users_lower:
        print(f"The name {user} is avaliable, pick another username!")
    else:
        print(f"Yes, {user} you are in current users right now!")


# Solution 5.11
# Name: Ordinal numbers
numbers=list(range(1,10))
for number in numbers:
    if number == 1:
        print(f"\n{number}st")
    elif number == 2:
        print(f"\n{number}nd")
    elif number == 3:
        print(f"\n{number}rd")
    else:
        print(f"\n{number}th")
