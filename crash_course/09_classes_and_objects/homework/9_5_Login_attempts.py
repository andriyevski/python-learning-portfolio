# Homework from file tasks/9_5_Login_attempts.md
## Task ## : 9.5
# 9_5_Login_attempts
from typing import Dict, Any

class Users():
    """
    Represents a user profile with core attributes and optional extra info.
    """
    def __init__(self, first_name: str, last_name: str, age: int, country: str, **user_info: Dict[str,Any]) -> None:
        """
        Think about all info what we need in class about user
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        self.login_attempts = 0
        self.user_info = user_info

    def describe_user(self) -> None:
        """ get all info about user """
        for key, info in self.user_info.items():
            print(f"{key} : {info}")

    def greet_user(self) -> None:
        """ Print 'Welcome' to user """
        print(f"Hello {self.first_name}, nice to see you again!")

    def increment_login_attempts(self) -> None:
        self.login_attempts+=1
        print(f"You login {self.login_attempts} times!")

    def reset_login_attempts(self) -> None:
        self.login_attempts = 0
        print(f"Your logining times was reset to {self.login_attempts}!")

first_user = Users('Mike','Tyson', 56, 'Usa', win=56, lose=4)
first_user.greet_user()
first_user.describe_user()

first_user.increment_login_attempts()
first_user.increment_login_attempts()
first_user.reset_login_attempts()
