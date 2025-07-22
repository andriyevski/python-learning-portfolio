# Work with Slices
players = ['charles','martina','michael','eli']
print(players[:3])
## Code ## : ['charles','martina','michael']

# Or start slices from 2 index
print(players[2:])
## Code ##: ['michael','eli']

# Distinct index ( last three index )
print(players[-3:])
## Code ## : ['martina','michael','eli']

# Looping through the contents of a segment
players = ['charles','martina','michael','florence','eli']

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
## Code ## : Here are the first three players on my team:
# Charles
# Martina
# Michael
