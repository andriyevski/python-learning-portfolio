import json

def ask_numb():
    question = input("Enter your favorite number: ")
    return int(question)

def create_answer():
    question = ask_numb()
    with open('favorite_number.json', 'w', encoding = "utf-8") as f:
        json.dump(question, f)
    print(f"Your favorite number {question} i am remember!")

def read_number():
    try:
        with open('favorite_number.json') as f:
            result = json.load(f)
        print(f"Your favorite number {result} i am remember!")
    except FileNotFoundError:
        create_answer()

if __name__ == "__main__":
    read_number()
