# Homework from file tasks/8_6_cities_names.md
## Task ## : 8.6
# 8_6_cities_names

def city_country(city: str, country: str) -> str:
    """
    return your city and country!
    """
    formatted_city_country = f"{city}, {country}"
    return formatted_city_country.title()


def interactive_city_country():
    """
    Return a formatted string in the form 'City, Country', with title case.
    """
    while True:
        """
        Ask user which city and country he was and quit = `q`
        """
        city_i = input("\nEnter your city:")
        # Ask user for city and country until they type 'q' to quit
        if city_i.lower() == 'q':
            break

        country_i = input("\nEnter your country:")
        if country_i.lower() == 'q':
            break


        formatted_answer = city_country(city_i, country_i)
        print(f"\nYou are from : {formatted_answer}")


# Test calls
print(city_country("santiago", "chile"))
print(city_country("kyiv", "ukraine"))
print(city_country("osaka", "japan"))

# interactive input city and country
interactive_city_country()
