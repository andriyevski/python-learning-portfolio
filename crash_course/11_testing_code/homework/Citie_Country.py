def city_country(citie: str, country: str) -> str :
    """ Return Citie and Country in one string with Title """
    citie = citie.lower()
    citie = citie.title()
    # Clear format to lower case and give Title case
    country = country.lower()
    country = country.title()
    return f"Citie: {citie}, Country: {country}"

print(city_country('kYiv','ukraine'))
