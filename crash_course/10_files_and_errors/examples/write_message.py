filename = 'programming.txt'

# some_list = [1,2,3]
# some_list += some_list+['I love programming!\n']
# 'w' - like 'write' in list -> some_list+['I love programming!\n']
with open(filename, 'w', encoding = 'utf-8') as file_object:
    file_object.write("I love programming!\n")
    file_object.write("I love creating new games.\n")

# 'a' - like 'append' in list -> append('I love programming!\n')
with open(filename, 'a', encoding = 'utf-8') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I also love finding meaning in large datasets.\n")
