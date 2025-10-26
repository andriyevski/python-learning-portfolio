# Homework from file tasks/10_9_Silent_Error.md
## Task ## : 10.9
# 10_9_Silent_Error
def read_file(filename):
    with open(filename, encoding = 'utf-8') as f:
        result_file = f.read()
        return result_file

def check_file(filename):
    try:
        print(read_file(filename))
    except FileNotFoundError as e:
        pass

if __name__ == "__main__":
    files = ('Not_greated_file.txt','cats.txt',)
    for file in files:
        check_file(file)
