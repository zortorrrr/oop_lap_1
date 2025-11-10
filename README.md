# Data Processing Lab

## Lab Overview
This lab demonstrates a simple and organized data processing program that loads data from a CSV file, filters it based on conditions, and performs aggregation operations such as averages and maximums. It applies an object-oriented design to separate file loading from data manipulation, making the code cleaner and easier to maintain.

**Key Features**
- CSV file loading and parsing  
- Filtering using lambda functions  
- Aggregations (average, max, count, etc.)  
- Supports method chaining for combined queries  
- Handles numeric type conversion safely  

---

## Project Structure

The project includes two main classes:  
- **DataLoader** – Handles reading and parsing CSV files  
- **Table** – Performs filtering, aggregation, and data storage  

---

## Design Overview

### DataLoader Class
**Purpose:** Reads CSV files and converts them into Python data structures.  
**Attributes:**  
- `base_path`: Directory where CSV files are located  

**Main Methods:**  
- `__init__(self, base_path=None)` – Initializes the loader with a default or custom path  
- `load_csv(self, filename)` – Reads a CSV file and returns a list of dictionaries representing rows  

### Table Class
**Purpose:** Manages tabular data and supports filtering and aggregation.  
**Attributes:**  
- `name`: Table name  
- `dict_list`: List of dictionaries containing data rows  

**Main Methods:**  
- `__init__(self, name, dict_list)` – Creates a table with a given name and dataset  
- `filter(self, condition_func)` – Returns a new table filtered by a condition  
  Example: `table.filter(lambda x: x['country'] == 'Germany')`  
- `aggregate(self, agg_func, column_name)` – Performs an aggregation on a specific column  
  Automatically converts string values to floats for numeric operations  

---

## How to Run
**Requirements:** Python 3.6+ and a `Cities.csv` file in the same directory.  

**Example CSV:**
```csv
city,country,temperature
Berlin,Germany,10.5
Madrid,Spain,15.2
Rome,Italy,18.7
...
