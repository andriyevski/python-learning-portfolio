import json

def ask_numb():
    question = input("Enter your favorite number: ")
    return int(question)

def save_numb(numb):
    with open('number.json', 'w', encoding = 'utf-8') as f:
        json.dump(numb, f)

def read_numb():
    with open('number.json') as f:
        return json.load(f)


if __name__ == "__main__":
    try:
        print(read_numb())
    except FileNotFoundError:
        save_numb(ask_numb())
