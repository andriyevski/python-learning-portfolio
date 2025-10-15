# Homework from file tasks/10_5_Syrvey.md
## Task ## : 10.5
# 10_5_Syrvey
survey_list = 'survey_list.txt'

while True:
    survey_answer = input("For exit try: 'q','exit'\nEnter why you like programming?\n\nEnter your reason: ")

    try:
        if survey_answer.lower() in ('q','exit'):
            print("\n\nGood Bye!")
            break
        else:
            with open(survey_list, 'a', encoding = "utf-8") as f:
                result = f.write(survey_answer.strip()+"\n")
                print("\n Reason : "+survey_answer.strip()+"\n")
    except Exception as e:
        print(f"Error! {e}")
