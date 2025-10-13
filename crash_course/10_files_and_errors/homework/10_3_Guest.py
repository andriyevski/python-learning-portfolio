# Homework from file tasks/10_3_Guest.md
## Task ## : 10.3
# 10_3_Guest
filename = 'guest.txt'

name = input("Enter your name: ")

with open(filename, 'w', encoding = 'utf-8') as file_obj:
    file_obj.write(name)
