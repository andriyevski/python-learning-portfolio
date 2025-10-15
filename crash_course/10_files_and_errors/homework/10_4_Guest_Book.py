# Homework from file tasks/10_4_Guest_Book.md
## Task ## : 10.4
# 10_4_Guest_Book
filename = 'guest_book.txt'

while True:
    name = input("Enter your name: ").strip()

    # if name == 'q' or name == 'Q' or name == 'exit' or name == 'Exit':
    if name.lower() in ('q','exit',):
        print("\nGood Bye!\n")
        break
    elif name:
        with open(filename, 'a', encoding = 'utf-8') as file_obj:
            file_obj.write(name+'\n')
            print(name+'\n')
