def greet_users(names):
    """
    Print welcome to every users
    """
    for name in names:
        msg = f"Hello, {name.title()}"
        print(msg)


username = ['hahaha', 'ty', 'margo']
greet_users(username)
