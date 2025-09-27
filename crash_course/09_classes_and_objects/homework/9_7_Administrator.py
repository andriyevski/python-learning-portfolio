# Homework from file tasks/9_7_Administrator.md
## Task ## : 9.7
# 9_7_Administrator

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
        self.user_info = user_info

    def describe_user(self) -> None:
        """ get all info about user """
        for key, info in self.user_info.items():
            print(f"{key} : {info}")

    def greet_user(self) -> None:
        """ Print 'Welcome' to user """
        print(f"Hello {self.first_name}, nice to see you again!")

class Admin(Users):
    """ It is user too """
    def __init__(self, first_name, last_name, age, country, privilege):
        super().__init__(first_name, last_name, age, country)
        self.privilege = privilege

    def show_privileges(self):
        """ print privileges of user  """
        privileges = [1, 2, 3]
        count_value = 0

        for lvl in privileges:
            if len(privileges) >= 0 and count_value <= 0:
                count_value +=1
                print(f"\nUser: {self.first_name} {self.last_name} is Admin and can:")
            if lvl == 1:
                print(f"- allowed to add messages")
            if lvl == 2:
                print(f"- It is allowed to delete users")
            if lvl == 3:
                print(f"- It is allowed to ban users")
            if lvl == "" or lvl == None:
                print(f"User: {self.first_name} {self.last_name} is just default User!")

new_admin_user = Admin('Elon','Musk', 37, "Usa", [1,2])
new_admin_user.greet_user()
new_admin_user.describe_user()
new_admin_user.show_privileges()
