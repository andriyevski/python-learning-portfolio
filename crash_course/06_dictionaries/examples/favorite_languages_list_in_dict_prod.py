# How work list in dict
from typing import Dict


Fav_Languages= Dict[str,list[str]]

def get_favorite_languages_users() -> Fav_Languages:
    """All users and ther favorite lang"""
    return {
        'jen':['python','ruby'],
        'sarah':['c'],
        'edward':['ruby','go'],
        'phil':['python','haskell'],
    }

def print_names_languages(users: Fav_Languages) -> None:
    """Print all users and his languages"""
    if users:
        for name, languages in users.items():
            print(f"\n{name.title()}'s favorite languages are:")
            for language in languages:
                print(f"\t{language.title()}")
    else:
        print("\nDict error from DB")


if __name__ =="__main__":
    print_names_languages(get_favorite_languages_users())
