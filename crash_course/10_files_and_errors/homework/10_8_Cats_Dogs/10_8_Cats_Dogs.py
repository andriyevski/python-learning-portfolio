# Homework from file tasks/10_8_Cats_Dogs.md
## Task ## : 10.8
# 10_8_Cats_Dogs
def read_file(filename):
    with open(filename, encoding = 'utf-8') as f:
        result_file = f.read()
        return result_file

def check_file(filename):
    try:
        print(read_file(filename))
    except FileNotFoundError as e:
        print(f"File not found! -> {e.filename}")

if __name__ == "__main__":
    files = ('dogs.txt','cats.txt',)
    for file in files:
        check_file(file)
