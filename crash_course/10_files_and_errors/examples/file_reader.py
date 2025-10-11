with open("pi_digits.txt") as file_objects:
    contents = file_objects.read()
    print(contents.rstrip())


"""
Or use this to absolute path

file_path = '/home/ehmatthes/other_files/text_files/имя_файла.txt'
with open(file_path) as file_object:
"""

filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.replace(" ",""))
