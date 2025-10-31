def get_formatted_name(first, last):
    """ Build formatting full name """
    full_name = f"{first} {last}"
    return full_name.title()

print(get_formatted_name("James", "Armstrong"))
