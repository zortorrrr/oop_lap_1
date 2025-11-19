import csv
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


class DB:
    """Simple in-memory database."""

    def __init__(self):
        self.tables = {}

    def insert(self, table):
        self.tables[table.table_name] = table

    def search(self, name):
        return self.tables.get(name, None)


class Table:
    def __init__(self, table_name, table):
        self.table_name = table_name
        self.table = table

    def __str__(self):
        return f"{self.table_name}:" + str(self.table)

    def filter(self, func):
        filtered = [row for row in self.table if func(row)]
        return Table(self.table_name, filtered)

    def aggregate(self, func, column):
        values = []
        for row in self.table:
            try:
                values.append(float(row[column]))
            except ValueError:
                values.append(row[column])
        return func(values)

    def join(self, other_table, key):
        """
        Inner join on the given key.
        Keeps values from the left table, and adds only non-duplicate
        columns from the right table.
        """
        joined = []
        lookup = {}

        # Index other_table by key
        for r in other_table.table:
            lookup.setdefault(r[key], []).append(r)

        for row in self.table:
            k = row.get(key)
            if k in lookup:
                for r in lookup[k]:
                    merged = dict(row)
                    for col, val in r.items():
                        if col != key and col not in merged:
                            merged[col] = val
                    joined.append(merged)

        return Table(self.table_name + "_joined_" + other_table.table_name, joined)


# ------------------ TEST CODE ------------------

loader = DataLoader()

cities = loader.load_csv('Cities.csv')
table1 = Table('cities', cities)

countries = loader.load_csv('Countries.csv')
table2 = Table('countries', countries)

my_DB = DB()
my_DB.insert(table1)
my_DB.insert(table2)

my_table1 = my_DB.search('cities')
print("List all cities in Italy:")
my_table1_filtered = my_table1.filter(lambda x: x['country'] == 'Italy')
print(my_table1_filtered)
print()

print("Average temperature for all cities in Italy:")
print(my_table1_filtered.aggregate(lambda x: sum(x) / len(x), 'temperature'))
print()

my_table2 = my_DB.search('countries')
print("List all non-EU countries:")
my_table2_filtered = my_table2.filter(lambda x: x['EU'] == 'no')
print(my_table2_filtered)
print()

print("Number of countries that have coastline:")
print(
    my_table2.filter(lambda x: x['coastline'] == 'yes')
    .aggregate(lambda x: len(x), 'coastline')
)
print()

my_table3 = my_table1.join(my_table2, 'country')
print("First 5 entries of the joined table (cities and countries):")
for item in my_table3.table[:5]:
    print(item)
print()

print("Cities whose temperatures are below 5.0 in non-EU countries:")
my_table3_filtered = (
    my_table3.filter(lambda x: x['EU'] == 'no')
    .filter(lambda x: float(x['temperature']) < 5.0)
)
print(my_table3_filtered.table)
print()

print("The min and max temperatures for cities in EU countries that do not have coastlines")
my_table3_filtered = (
    my_table3.filter(lambda x: x['EU'] == 'yes')
    .filter(lambda x: x['coastline'] == 'no')
)
print("Min temp:", my_table3_filtered.aggregate(lambda x: min(x), 'temperature'))
print("Max temp:", my_table3_filtered.aggregate(lambda x: max(x), 'temperature'))
print()
