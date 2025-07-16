# Practice of chapter 2
## Change guest list
#
top_guest = ['Mike Tyson','Elon Musk','Tomas Edison']
print(f'Hello {top_guest[0]}, welcome to the evening of meeting!')
print(f'Hello {top_guest[1]}, welcome to the evening of meeting!')
print(f'Hello {top_guest[2]}, welcome to the evening of meeting!')

# Or use something like this, more Pythonic
for guest in top_guest:
    print(f'Hello {guest}, welcome to the evening of meeting!')

# Guest who can't come to meeting we need change
print(f"Sorry but {top_guest[2]} can't come to meeting!")
top_guest[2] = 'Bill Gates'
for guest in top_guest:
    print(f'Now is new list of guest to meeting support: {guest}')

# Or you can use Remove
top_guest.remove('Mike Tyson')
top_guest.append('Cristiano Ronaldo')
for guest in top_guest:
    print(f'Welcome to meeting {guest} and nice to meeting!')

## Change more guest list
#
top_guest = ['Mike Tyson','Elon Musk','Tomas Edison']
print(f'Added new guest Mark Zukerberg')
top_guest.insert(0,'Mark Zukerberg')
top_guest.insert(2,'Roy Jones')
top_guest.append('Oleksandr Usyk')
for guest in top_guest:
    print(f'Welcome to meeting mr.{guest}, nice to meet you!')

## Change to more short list of guests
#
print(f'Sorry, but only two guest can sit on the table in meeting!')
print(f'Sorry, but guest {top_guest.pop()} do not come to meeting!')
for guest in top_guest:
    print(f'Hello mr.{guest}, we are waiting for you on meeting tonight!')
print(f'\n {top_guest[4]}')
del top_guest[4]
del top_guest[3]
del top_guest[2]
print(top_guest)
