## Work with for in list
#
magicians = ['alice','david','carolina']
for magician in magicians:
    print(magician+".\n")


##If you forgot to indent, print one times only
#
magicians = ['alice','david','carolina']
for magician in magicians:
    print(magician.title()+", That was a great trick!")
print(f"I can't wait to see your next trick, {magician.title()}.\n")

## If we have a one more tab
#
magicians = ['Aliace','David','Carolina']
for magician in magicians:
    print(f'{magician.title()}, that was a great trick!')
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
    # Logical error - we take last name in ovetabundance of list
    print(f"Thank you everyone, that was a great magic SHOW!{magician.title()}")
