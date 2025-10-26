# Homework from file tasks/10_7_Calculator.md
## Task ## : 10.7
# 10_7_Calculator
quit_param = ['q', 'exit']

while True:
    """ We need to work all time ! """
    try:
        question_one = input("Write some int to sum: ").strip()
        if question_one.lower() in quit_param:
            print("Good Bye bro!")
            break
        question_two = input(f"Enter second sum -> {question_one} + ...").strip()
        if question_two.lower() in quit_param:
            print("Good Bye bro!")
            break
        else:
            sum_result = int(question_one)+int(question_two)
            print(type(sum_result))
            print(f"# {question_one} + {question_two} = {sum_result}")
    except ValueError:
        print("No write pls int value only! -> 'ValueError'")
