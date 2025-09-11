def greet_user():
    """Print hello message"""
    print("Hello!")

greet_user()


def greet_user_2(username):
    """ Print Username hello message """
    print(f"Hello, {username.title()}")

greet_user_2("Serhii")

def get_formatted_name(first_name, last_name):
    """
    return formatted name
    """
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name:")
    if f_name == 'q':
        break

    l_name = input("Last name:")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}")
