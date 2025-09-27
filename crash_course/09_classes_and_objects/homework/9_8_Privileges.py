# Homework from file tasks/9_8_Privileges.md
## Task ## : 9.8
# 9_8_Privileges
from typing import Dict, Any

class Users:
    def __init__(self, first_name: str, last_name: str, age: int, country: str, **user_info: Dict[str, Any]) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        self.user_info = user_info

    def describe_user(self) -> None:
        for key, info in self.user_info.items():
            print(f"{key} : {info}")

    def greet_user(self) -> None:
        print(f"Hello {self.first_name}, nice to see you again!")

class Privileges:
    def __init__(self, privileges: list[str]) -> None:
        self.privileges = privileges

    def show_privileges(self) -> None:
        print("\nAdmin privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

class Admin(Users):
    def __init__(self, first_name, last_name, age, country, **user_info):
        super().__init__(first_name, last_name, age, country, **user_info)
        self.privileges = Privileges([
            "can add messages",
            "can delete users",
            "can ban users"
        ])


new_admin_user = Admin('Elon', 'Musk', 37, "USA")
new_admin_user.greet_user()
new_admin_user.describe_user()
new_admin_user.privileges.show_privileges()
