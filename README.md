## 1. Lab Overview
This lab extends the data processing system from Laboratory 2 by introducing a simple in-memory **database** and enabling operations that involve **multiple tables**.  
In real-world data processing, datasets often share common attributes. This lab demonstrates how two tables can be **joined** using a shared key (e.g., `country`).  

The objectives of this lab are:
- To store and manage multiple tables using a database-like structure.
- To implement an **inner join** between two tables.
- To continue using functional-style operations such as **filter** and **aggregate**.
- To work with two datasets (`Cities.csv` and `Countries.csv`) and analyze them together.

---

## 2. Project Structure
oop_lab_3/
├── data_processing.py # Contains DataLoader, DB, Table, join/filter/aggregate, and test code
├── Cities.csv # Table of cities with temperature and coordinates
├── Countries.csv # Table of countries with EU and coastline attributes
└── README.md # Documentation file (this file)


---

## 3. Design Overview

### 3.1 DataLoader Class
**Purpose:**  
Load CSV files and return their contents as a list of dictionaries.

**Attributes:**  
- `base_path`: Directory where data files are located.

**Key Methods:**  
- `load_csv(filename)`  
  - Reads the CSV file using `csv.DictReader`.  
  - Returns a Python list of dictionaries representing table rows.

---

### 3.2 DB Class  
**Purpose:**  
A lightweight in-memory database used to store and retrieve multiple tables.

**Attributes:**  
- `tables`: A dictionary that maps table names to `Table` objects.

**Key Methods:**  
- `insert(table)`  
  Stores a table in the database using its `table_name` as the key.  
- `search(name)`  
  Retrieves a stored table by its name. Returns `None` if not found.

---

### 3.3 Table Class  
**Purpose:**  
Represents a table of data and provides key data-processing operations such as filtering, aggregation, and joining.

**Attributes:**  
- `table_name`: Name of the table.  
- `table`: List of dictionaries (rows).

**Key Methods:**

- `filter(func)`  
  - Applies a condition function (usually a lambda expression).  
  - Returns a new `Table` containing only the rows that satisfy the condition.  

- `aggregate(func, column)`  
  - Collects all values from a given column.  
  - Automatically converts numeric values to `float` when possible.  
  - Applies an aggregation function such as `sum`, `min`, `max`, or `len`.  

- `join(other_table, key)`  
  - Performs an **inner join** between this table and another table based on a shared key.  
  - Combines matching rows and merges attributes without overwriting duplicate keys.  
  - Returns a new `Table` representing the joined result.

---

## 4. How to Test and Run the Code

### Requirements
- Python 3.6 or higher  
- `Cities.csv` and `Countries.csv` placed in the same directory as `data_processing.py`

### Running the Program
Open a terminal in the project directory and run:

```bash
python data_processing.py
Expected Outputs
The test code included in data_processing.py will display:
All cities in Italy
Average temperature of Italian cities
All non-EU countries
Number of countries with coastlines
First five rows of the joined cities × countries table
Cities below 5°C in non-EU countries
Minimum and maximum temperatures in EU countries with no coastline
All outputs should match the example shown in the official lab instructions.

Summary
This lab introduces cross-table operations using object-oriented programming principles.
By incorporating a simple database and a join mechanism, the system becomes capable of analyzing multiple datasets together.
The concepts practiced here form a foundation for understanding relational databases and more advanced data processing techniques in future courses.