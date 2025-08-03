# Favorite language in pythonic style!
favorite_languages = {
    'yen': 'python',
    'sarah': 'c',
    'edward':'ruby',
    'phil': 'python',
}

print(favorite_languages['sarah'])

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

# work with keys()
for name in favorite_languages.keys():
    print(name.title())


# Friends task
friends = ['phil','sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, i see you love {language}!")
