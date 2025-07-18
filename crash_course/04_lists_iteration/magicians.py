## Work with for in list
#
magicians = ['alice','david','carolina']
for magician in magicians:
    print(magician)


##If you forgot to indent
#
magicians = ['alice','david','carolina']
for magician in magicians:
    print(magician.title()+", That was a great trick!")
print(f"I can't wait to see your next trick, {magician.title()}.\n")
