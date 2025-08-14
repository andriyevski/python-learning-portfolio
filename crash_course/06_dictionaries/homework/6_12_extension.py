# Homework from file tasks/extensions.md
## Task ## : 6.11
# 6_12_ extensions
cities = {
    "Tokyo": {
        "country": "Japan",
        "population": 14_000_000,
        "fact": "Tokyo is the most populous metropolitan area in the world.",
        "founded": 1603,
        "landmark": "Tokyo Skytree"
    },
    "Paris": {
        "country": "France",
        "population": 2_100_000,
        "fact": "Paris is known as the 'City of Light' and is home to the Eiffel Tower.",
        "founded": -52,  # Approximate founding by Romans
        "landmark": "Eiffel Tower"
    },
    "Chernivtsi": {
        "country": "Ukraine",
        "population": 260_000,
        "fact": "Chernivtsi is often called 'Little Vienna' for its architecture and cultural heritage.",
        "founded": 1408,
        "landmark": "Chernivtsi National University"
    }
}

for city, info in cities.items():
    print(f"\n🏙️ {city}")
    print("-" * (len(city) + 4))
    print(f"📍 Country:     {info['country']}")
    print(f"👥 Population:  {info['population']:,}")
    print(f"📅 Founded:     {info['founded']}")
    print(f"📌 Landmark:    {info['landmark']}")
    print(f"💡 Fact:        {info['fact']}")
