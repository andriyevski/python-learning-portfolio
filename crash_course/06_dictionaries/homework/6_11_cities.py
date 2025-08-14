# Homework from file tasks/cities.md
## Task ## : 6.11
# 6_11_ cities
cities = {
    "Tokyo": {
        "country": "Japan",
        "population": 14_000_000,
        "fact": "Tokyo is the most populous metropolitan area in the world."
    },
    "Paris": {
        "country": "France",
        "population": 2_100_000,
        "fact": "Paris is known as the 'City of Light' and is home to the Eiffel Tower."
    },
    "Chernivtsi": {
        "country": "Ukraine",
        "population": 260_000,
        "fact": "Chernivtsi is often called 'Little Vienna' for its architecture and cultural heritage."
    }
}

for city, info in cities.items():
    print(f"\n🏙️ {city}")
    print(f"  Country: {info['country']}")
    print(f"  Population: {info['population']:,}")
    print(f"  Fact: {info['fact']}")
