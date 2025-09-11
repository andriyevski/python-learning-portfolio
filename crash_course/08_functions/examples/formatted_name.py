def get_formatted_name(first_name, last_name,middle_name=''):
    """
    returned formatted name
    """
    if middle_name:
        full_name = f"{first_name} {last_name} {middle_name}"
        return full_name.title()
    else:
        full_name = f"{first_name} {last_name}"
        return full_name.title()

musician = get_formatted_name('jimi','hendrix')
musician_2 = get_formatted_name('jimi','hendrix','floyd')
print(musician)
print(musician_2)
