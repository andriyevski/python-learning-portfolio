# Use list
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
#Shell#:  ['honda','yamaha','suzuki']

# Change 'honda' to 'ducati' in list motorcycles in index - 0
motorcycles[0] = 'ducati'
print(motorcycles)
#Shell#:  ['ducati','yamaha','suzuki']

# Delete all value in list
motorcycles = []
print(motorcycles)
#Shell#: []

# Add elements to list
motorcycles = ['honda','yamaha','suzuki']
motorcycles.append('ducati')
print(motorcycles)
#Shell#: ['honda','yamaha','suzuki','ducati']
# or use insert
# Index position:
# motorcycles=[   0    ,   1    ,   2   ]
motorcycles = ['honda','yamaha','suzuki']
motorcycles.insert(0,'ducati')
# motorcycles=[   0    >   1    >>   2   ]
# motorcycles=[   0    ,   1    ,   2   ,   3   ]
print(motorcycles)
#Shell#:     ['ducati', 'honda', 'yamaha', 'suzuki']

# Delete elements in list by index
# Del -> index [] in list
motorcycles = ['Honda','Yamaha','Suzuki']
del motorcycles[2]
print(motorcycles)
#Shell#: ['Honda', 'Yamaha']

# Delete element with use pop()
motorcycles = ['Honda','Yamaha','Suzuki']
motorcycles.pop()
print(motorcycles)
#Shell#: ['Honda', 'Yamaha']

# Delete last element in list and greate new
motorcycles = ['Honda','Yamaha','Suzuki']
poped_motorcycles = motorcycles.pop()
# poped_motorcycles is str
print(poped_motorcycles)
#Shell#: Suzuki

# Last buy motorcycles
motorcycles = ['Honda','Yamaha','Suzuki']
last_owned = motorcycles.pop()
print(f"The last motorcycles i owned was {last_owned.title()}")
#Shell#: Suzuki

# Pick from any one index in motorcycles
motorcycles = ['Honda','Yamaha','Suzuki']
first_owned = motorcycles.pop(0)
print(f"Pick first index in motorcycles is {first_owned}")
#Shell#: Pick first index in motorcycles is Honda

# Delete elements by value
motorcycles = ['Honda', 'Yamaha','Suzuki']
motorcycles.remove('Yamaha')
print(motorcycles)
#Shell#: ['Honda', 'Suzuki']

# Delete element and show him
motorcycles = ['Honda', 'Yamaha','Suzuki']
too_expensive  = 'Suzuki'
motorcycles.remove(too_expensive)
print(f"Thi is {too_expensive} too expensive for me!")
#Shell#: This is Suzuki too expensive for me!
# Remove delete only one time one first word ! Use while if you want delete all!
