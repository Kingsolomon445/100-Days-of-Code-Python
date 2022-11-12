# A travel log program

travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


def add_new_country(count, times, city):
    new_dictionary = {"country": count, "visits": times, "cities": city}
    travel_log.append(new_dictionary)
    print(travel_log)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
