msg = "Message for people!"

var_1 = 0
var_2 = 1

# Just ( _ ) Space button
tab_text = "\n"

# Simple print
print("var_1:", {var_1}, "\var_2:", {var_2}, "\nmsg:", {msg})
print(tab_text)

# F-string print
print(f"msg:{msg} \nvar_1:{var_1} \nvar_2:{var_2}")
print(tab_text)

# or debuging
print(f"\nFirst Debug:\n{msg=}\n{var_1=}\n{var_2=}")

#or
print(f"""
\nSecond Debug:\n
{msg=}\n
{var_1=}\n
{var_2=}
""")

# F-string (When too much row)
print(f"""
msg: {msg}
var_1: {var_1}
var_2: {var_1}
\n\n
""")

# Check type of object
print(f"msg: {msg} - {type(msg)}")
print(f"var_1: {var_1} - {type(msg)}")
print(f"var_2: {var_2} - {type(var_2)}")

# Check id object
print(f"\nmsg: {msg}:\n id:{id(msg)}")