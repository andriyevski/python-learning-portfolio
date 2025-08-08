# Homework from file tasks/home_pets.md
## Task ## : 6.8
# 6_8_home_pets

barsic = {
    'type' : 'canadian sfinx',
    'age': 2,
    'sex':'male',
    'vacinated':'yes'
}

bob = {
    'type' : 'britan cat',
    'age': 8,
    'sex':'female',
    'vacinated':'no'
}

rex = {
    'type' : 'persian cat',
    'age': 1,
    'sex':'male',
    'vacinated':'no'
}

cats = [barsic, bob, rex]
for cat in cats:
    print(f"Type: {cat['type']}\nAge: {cat['age']}\nsex: {cat['sex']}\nVacinated: {cat['vacinated']}\n")
