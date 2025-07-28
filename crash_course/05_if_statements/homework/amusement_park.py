# Solution for homework
age = int(input("Your age? \n Write age:"))
if age < 4:
    print(f"\nYour age is {age} so you cant come free...")
elif age < 18:
    print(f"\nYour age is {age} so you must paid : $25...")
else:
    print(f"\nYour age is {age} so you must paid : $40...")
