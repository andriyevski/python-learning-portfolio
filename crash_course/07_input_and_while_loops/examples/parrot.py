promt = input("Tell me something, and i will repeat it back to you: ")
promt +="\nEnter 'Quit' to end the program.\n"
message =""

# while message != 'quit':
#     message = input(promt)
#
#     if message != 'quit':
#         print(message)
active = True
while active:
    message = input(promt)

    if message == 'quit':
        active = False
    else:
        print(message)
