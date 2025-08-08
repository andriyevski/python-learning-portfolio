# Homework from file tasks/peoples.md
## Task ## : 6.7
# Peoples
from typing import Dict


Peoples_Dict = Dict[str,str]


def get_peoples() -> Peoples_Dict:
    """List with all users in dict"""
    return  {
        'first_name':'George',
        'last_name':'Granovsky',
        'age':'38',
        'city':'Chicago',
    }

def print_peoples(users: Peoples_Dict) -> None:
    """Just print all users"""
    print(f"First name: {users['first_name']}\n")
    print(f"Last name: {users['last_name']}\n")
    print(f"Age: {users['age']}\n")
    print(f"City: {users['city']}\n")


if __name__ == "__main__":
    print_peoples(get_peoples())
