import csv
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))
)

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

# Print first 5 cities only
for city in cities[:5]:
    print(city)


def filter(condition, dict_list):
    temps = []
    for item in dict_list:
        if condition(item):
            temps.append(item)
    return temps


def aggregate(aggregation_key, aggregation_function, dict_list):
    temps = []
    for item in dict_list:
        try:
            temps.append(float(item[aggregation_key]))
        except ValueError:
            temps.append(item[aggregation_key])
    return aggregation_function(temps)


# Print the average temperature of all the cities
print("The average temperature of all the cities:")
my_value = aggregate("temperature", lambda x: sum(x) / len(x), cities)
print(my_value)
print()

# Print all cities in Germany
print("All cities in Germany:")
filter_list = filter(lambda x: x["country"] == "Germany", cities)
for city in filter_list:
    print(city["city"], end=" ")
print()

# Print all cities in Spain with a temperature above 12°C
print("All cities in Spain with a temperature above 12°C:")
my_cities = filter(
    lambda x: x["country"] == "Spain" and float(x["temperature"]) > 12.0,
    cities
)
cities_list = [
    [city["city"], city["country"], city["temperature"]]
    for city in my_cities
]
for city in cities_list:
    print(city)
print()

# Count the number of unique countries
print("The number of unique countries:")
my_value = aggregate("country", lambda x: len(set(x)), cities)
print(my_value)
print()

# Print the average temperature for all the cities in Germany
print("The average temperature for all the cities in Germany:")
my_value = aggregate(
    "temperature",
    lambda x: sum(x) / len(x),
    filter(lambda x: x["country"] == "Germany", cities)
)
print(my_value)
print()

# Print the max temperature for all the cities in Italy
print("The max temperature for all the cities in Italy:")
my_value = aggregate(
    "temperature",
    lambda x: max(x),
    filter(lambda x: x["country"] == "Italy", cities)
)
print(my_value)
