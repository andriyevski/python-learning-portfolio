promt = input("Tell me something, and i will repeat it back to you: ")
promt +="\nEnter 'Quit' to end the program."
message =""

while message != 'Quit':
    message = input(promt)
    print(message)
