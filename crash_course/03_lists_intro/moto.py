# Use list
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
#Shell#:  ['honda','yamaha','suzuki']

# Change 'honda' to 'ducati' in list motorcycles in index - 0
motorcycles[0] = 'ducati'
print(motorcycles)
#Shell#:  ['ducati','yamaha','suzuki']

# Dellet all value in list
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

# Dell elements in list
