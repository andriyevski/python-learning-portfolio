# Define the filename containing digits of pi
filename = 'pi_million_digits.txt'

# Open the file and read its entire content into a string
with open(filename) as pi_digits:
    pi_digit = pi_digits.read()

# Print the total number of characters in the raw file
print(len(pi_digit))

# Print the full raw content (may be very large!)
print(pi_digit)

# Print the length and preview of the first 150 characters
print(len(pi_digit[:150]))
print(pi_digit[:150])

# Initialize an empty list to store cleaned characters
clear_pi_digit = []

# Iterate over each character in the raw string
# Remove spaces, newlines, and tabs, and add cleaned characters to the list
for line in pi_digit:
    clear_pi_digit += line.replace(" ", "").replace("\n", "").replace("\t", "")

# Print the type of the cleaned list (should be <class 'list'>)
print(type(clear_pi_digit))

# Join the list of characters into a single clean string
pi_digit = ''.join(clear_pi_digit)

# Print the first 11 digits of the cleaned pi string
print(f"{pi_digit[:11]}")
