import csv
import os
from pathlib import Path


class DataLoader:
    """Handles loading CSV data files."""

    def __init__(self, base_path=None):
        """Initialize the DataLoader with a base path for data files."""
        if base_path is None:
            self.base_path = Path(__file__).parent.resolve()
        else:
            self.base_path = Path(base_path)

    def load_csv(self, filename):
        """Load a CSV file and return its contents as a list of dictionaries."""
        filepath = self.base_path / filename
        data = []

        with filepath.open() as f:
            rows = csv.DictReader(f)
            for row in rows:
                data.append(dict(row))

        return data


class Table:
    """Represents a table of data with basic filtering and aggregation."""

    def __init__(self, name, dict_list):
        self.name = name
        self.dict_list = dict_list

    def filter(self, condition_func):
        """Return a new Table containing rows that match the condition."""
        filtered_data = [row for row in self.dict_list if condition_func(row)]
        return Table(self.name, filtered_data)

    def aggregate(self, agg_func, column_name):
        """Aggregate values of a specific column using the provided function."""
        temps = []
        for item in self.dict_list:
            try:
                temps.append(float(item[column_name]))
            except ValueError:
                temps.append(item[column_name])
        return agg_func(temps)


if __name__ == "__main__":
    loader = DataLoader()
    cities = loader.load_csv('Cities.csv')
    my_table = Table('cities', cities)

    # Average temperature of all cities
    avg_temp = my_table.aggregate(lambda x: sum(x) / len(x), 'temperature')
    print("Average temperature of all cities:")
    print(avg_temp)
    print()

    # All cities in Germany
    germany_cities = my_table.filter(lambda x: x['country'] == 'Germany')
    cities_list = [[c['city'], c['country']] for c in germany_cities.dict_list]
    print("All cities in Germany:")
    for city in cities_list:
        print(city)
    print()

    # All cities in Spain with temperature above 12°C
    spain_hot = my_table.filter(
        lambda x: x['country'] == 'Spain' and float(x['temperature']) > 12.0
    )
    spain_list = [
        [c['city'], c['country'], c['temperature']]
        for c in spain_hot.dict_list
    ]
    print("All cities in Spain with temperature above 12°C:")
    for city in spain_list:
        print(city)
    print()

    # Number of unique countries
    num_countries = my_table.aggregate(lambda x: len(set(x)), 'country')
    print("The number of unique countries is:")
    print(num_countries)
    print()

    # Average temperature of all cities in Germany
    avg_germany = my_table.filter(
        lambda x: x['country'] == 'Germany'
    ).aggregate(lambda x: sum(x) / len(x), 'temperature')
    print("Average temperature of all cities in Germany:")
    print(avg_germany)
    print()

    # Max temperature of all cities in Italy
    max_italy = my_table.filter(
        lambda x: x['country'] == 'Italy'
    ).aggregate(lambda x: max(x), 'temperature')
    print("Max temperature of all cities in Italy:")
    print(max_italy)
    print()
