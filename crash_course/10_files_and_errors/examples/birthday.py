filename = 'pi_million_digits.txt'

with open(filename) as file:
    pi_string = file.read()

pi_string = pi_string.replace(" ","").replace("\n", "").replace("\t","")
birthday = input("Enter your birthday , in the form mmddyy: ")
if birthday in pi_string:
    print("Yuor birthday appears in the first million digits of pi!")
else:
    print("Yuor birthday appears not in the first million digits of pi!")
