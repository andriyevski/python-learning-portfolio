# Homework from file tasks/human.md
## Task ## : 6.1
human = {
    'first_name':'Rocky',
    'last_name':'Stalone',
    'age':'38',
    'city':'chicago'
    }

print(f"Hello my name: {human['first_name']}\nMy lastname: {human['last_name']}\nMy age: {human['age']}\nMy city: {human['city']}")


## Task ## : 6.2
# Favorit numbers
favorite_numbers = {
    'eva': 1,
    'george': 5,
    'Serhii': 7,
    'roman': 0,
    'harison': 31,
}

for name in favorite_numbers:
    print(f"Favorite number of {name.title()} is {favorite_numbers[name]}")

## Task ## : 6.3
# Glossary
glossary = {
    'getting_started':'about python power',
    'list_intro':'about list working',
    'list_iteration':'explain how eteration list work',
    'if_statement':'How working conditions',
    'dictionaries':'how work this is so important object',
}

for name in glossary:
    print(f"\nChapter {name} explain - {glossary[name]}")
