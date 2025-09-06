# Homework from file tasks/7_10_vocation_dreem.md
## Task ## : 7.10
# 7_10_vocation_dreem

# QUESTION: Where he want to vocation ?
active = True
result = {}

while active:
    response = input("Do you want to answer the question? Type 'yes' or 'no': ")
    if response == 'no':
        for name in result:
            print(f"Name: {name}\nDream Vacation: {result[name]}\n")
        break
    elif response == 'yes':
        ask = input("What is your name: ")
        request = input("Enter your dream vacation location: ")
        result[ask] = request
