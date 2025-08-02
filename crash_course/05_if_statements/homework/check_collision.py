from typing import List,Set


def users_db() -> List[str]:
    # List of users from DB
    return ['Mike','Admin','Lora','Hovard','Antonio','john']

def new_users() -> List[str]:
    # List users from API or another DB
    return ['Henry','Zoe','Eva','Mark','aDMin','LoRa','Bob']

def check_collision(users: List[str]) -> Set[str]:
    # We change lists with users to lowercase to compare
    return {user.lower() for user in users}

def compare_users() -> None:
    # Compare usrs list with users in # DB:
    users_in_db = check_collision(users_db())
    new_extend_users = check_collision(new_users())

    if not users_in_db:
        print(f"The list with Users from DB is Empty!")
        return

    if not new_extend_users:
        print(f"The list with new Users to DB is Empty!")
        return

    for user in new_extend_users:
        if user in users_in_db:
            print(f"Username: {user} is already used! Change please!")
        else:
            print(f"Welcome, {user} you are registered now!")

if __name__ == "__main__":
    compare_users()
