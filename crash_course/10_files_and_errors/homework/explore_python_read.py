# Homework from file tasks/10_1_Examplore_Python_Read.md
## Task ## : 10.1
# 10_1_Examplore_Python_Read
filename = '../examples/file_reader.py'

with open(filename) as file:
    file_obj = file.readlines()

for line in file_obj:
    print(f"In Python you can..." + line)
