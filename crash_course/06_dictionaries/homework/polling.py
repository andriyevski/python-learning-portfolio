# Favorite language in pythonic style!
from typing import List,Dict

Lang_Dict = Dict[str,str]

def favorite_dict() -> Lang_Dict:
    """
    Dict with names and programming language
    """
    return {
        'yen': 'python',
        'sarah': 'c',
        'edward':'ruby',
        'phil': 'python',
    }

def peoples() -> List[str]:
    """
    List with people who are need to polling
    """
    peoples_list = [
        'Zohan',
        'joe',
        'yen',
        'pHil',
        'samanta'
    ]
    return peoples_list

def polling_collision(peoples: List[str], lang_list: Dict[str,str] ) -> None:
    """Check who need to polling and who polls"""
    lower_lang_list = [user.lower() for user in lang_list.keys()]

    for user in peoples:
        if user.lower() in lower_lang_list:
            print(f"Thank you for polls {user.title()}")
        else:
            print(f"Pleace {user.title()} you need to polls!")


if __name__ == "__main__":
    polling_collision(peoples(),favorite_dict())
