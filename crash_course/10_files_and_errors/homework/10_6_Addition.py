# Homework from file tasks/10_6_Addition.md
## Task ## : 10.6
# 10_6_Addition
quit = ['q','exit']
while True:
    try:
        print("To exit inpit 'q' or 'exit'!")
        question_first = input("Enter sum what do you want do addition: ")
        if question_first.lower() in quit:
            break
        question_second = input(f"Enter second sum addition to {question_first} + : ")
        if question_second.lower() in quit:
            break
        question_first = int(question_first)
        question_second = int(question_second)
        sum_result = int(question_first)+int(question_second)
        print(f"First sum: {question_first} + {question_second} second sum = {sum_result}")
    except ValueError:
        print("Enter please only 'int' value!")
        break
