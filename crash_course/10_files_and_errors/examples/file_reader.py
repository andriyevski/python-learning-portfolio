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


pi_string = ""
for line in lines:
    pi_string += line.replace(" ","")

print(pi_string)
real_len_string = len(line)
replace_len_string = len(pi_string)
print(f"Real sting len is: {real_len_string}")
print(line)
print(f"Change len string is: {replace_len_string}")
print(pi_string)
