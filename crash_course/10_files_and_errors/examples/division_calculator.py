# 
# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("No you can't divide by zero! -> 0")


print("Give me two numbers, and i'll divided them.")
print("Enter 'q' or 'exit' -> to Quit.")
quit_param = ('q','exit',)
while True:
    first_number = input("\nFirst Number: ")
    if first_number.lower() in quit_param:
        break

    second_number = input("Second Number: ")
    if second_number.lower() in quit_param:
        break

    try:
        answer = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("Why you use zero: 0 ?")
    except ValueError:
        print("Please enter valid integers!")
    else:
        print(int(answer))
