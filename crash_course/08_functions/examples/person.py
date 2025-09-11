def build_person(first_name, last_name, age = None):
    """
    return dict wit info ablout people!
    """
    person = {'first': first_name, 'last_name': last_name}
    if age is not None:
        person['age'] = age
    return person

musician = build_person('jimi', 'Hendrix', age=18)
print(musician)
