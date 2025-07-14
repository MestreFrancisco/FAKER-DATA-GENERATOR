# 📙 Base Table Builder

**Table Builder** is designed to help you create your own DataFrames using all the generators included in this project—as well as any custom logic you wish to apply. The module provides various tools for building tables flexibly. Once your table is ready, you can export it to CSV using the built-in methods.

The `Table` object has its own structure and behavior, so it's recommended to review this documentation carefully. Use the index below to navigate to specific sections.

- Return to README [Fake Data Generator](../../../../README.md)

## Index
- [📙 Base Table Builder](#-base-table-builder)
- [Attributes](#attributes)
- [How it Works](#how-it-works)
  - [dict_list](#dict_list)
  - [dfs](#dfs)
- [Quick Example](#quick-example)
- 🥟 [Example: `add_list_as_column()`](#example-of-the-add_list_as_column-method)
  - [Method Parameters](#-method-parameters)
  - [Usage Example](#-usage-example)
- 🥟 [Example: `add_options_as_column()`](#example-of-the-add_options_as_column-method)
  - [Quick Description](#--quick-description)
  - [Usage Example](#usage-example)
- 🥟 [Example: `to_df()`](#example-to_df)
  - [Parameters](#parameters)
  - [Usage Example](#usage-example)
- 🥟 [Example: `export_tables_to_csv()`](#example-export_tables_to_csv)
  - [Parameters](#-parameters)
  - [Usage Example](#-usage-example)
- 🥟 [Example: `add_persona_data_table()`](#example-add_persona_data_table)
  - [Parameters](#-parameters)
  - [Usage Example](#-usage-example)

## Attributes

| Attribute     | Type    | Description                                                                 |
|---------------|---------|-----------------------------------------------------------------------------|
| `tableName`   | `str`   | Name that identifies the table.                                             |
| `dict_list`   | `list`  | Empty list that will store data as dictionaries (row format).               |
| `dfs`         | `list`  | Empty list to store `DataFrame` objects (e.g., pages).                      |

The attributes `dfs` and `dict_list` are not initialized with data — they are populated using the methods provided by Table Builder.

```python
from Base.tabla_builder import Table
import polars as pl

table_ex = Table("Example table")
```

[Quick Example](#quick-example)

## How It Works

`Table` internally contains:

- `dict_list`: A list of lists of dictionaries, where each sublist represents a "table" (as a collection of rows in dictionary format).  
  This allows you to modify, expand, or add new columns independently to each "table". You can access them using an index.

```python
from Base.tabla_builder import Table
import polars as pl
from rich import print

table_ex = Table("Example table")

dict_list = [{"Name": "Francisco", "Age": 22}]

table_ex.add_dict(dict_list)

print(table_ex.dict_list[0])
```

- `dfs`: A list of DataFrame objects.  
  You populate this list by using the [`to_df`](#example-of-method-to_df) method.

This functionality is especially useful when you want to add new attributes to your generated data — for example: gender, favorite colors, salary ranges, etc.

## Quick Example

```python
from Base.tabla_builder import Table
from Gen import companies as gcomp
from rich import print

# Generate a fake company
company = gcomp.gen_obj_Company(1)[0]

# Get the number of employees in that company
employes = company.employee_count

# Create a new Table object
my_table = Table("my_first_table")

# Add employees as a new table inside the object
my_table.add_persona_data_table(employes)

# Add company data as a second table
my_table.add_dict(company.to_dict())

# Print all stored tables (in dict_list)
print(my_table.dict_list)
```

```python
{
    'id': 1,
    'name': np.str_('Sabrina Quintero Zapata'),
    'country': np.str_('Bahamas'),
    'age': 33,
    'mailcontact': 'sabrinaquinterozapata584@gmail.com'
    # +32 More fields...
},
{
    'best_place_to_work': False,
    'company_anual_budget': 63046.62000000001,
    'company_month_budget': 7005.180000000001,
    'company_value': '315.23K',
    'company_value_no_abbreviate': 315233.10000000003,
    'contact_email': 'greeneasyflow@falsegmail.com',
    'continent': 'Australia and Oceania',
    'country': 'Vanuatu',
    'employee_count': 13,
    # +12 More fields...
}
```
## Example of the `add_list_as_column()` Method

The `add_list_as_column()` method is used to add a new column to an existing table inside the `Table` class.  
This method takes a column name and a list of new values and assigns it as a new column in each row (dictionary) already in the table.

`Table` internally contains:

- `dict_list`: A list of lists, where each inner list represents a table (collection of dictionaries).
- `dfs`: A list of DataFrame objects (e.g., Polars or Pandas).

This function is especially useful when you want to add new attributes to your generated data, like gender, favorite colors, salaries, etc.

---

### Method Parameters

| Parameter        | Type     | Description                                                                                       |
|------------------|----------|---------------------------------------------------------------------------------------------------|
| `table_index`    | `int`    | Index of the table in `dict_list` where the new column will be added.                            |
| `colname`        | `str`    | Name of the new column. This will be used as the key in each dictionary row.                     |
| `new_values`     | `list`   | List of values to assign as the new column. Must match the table's length unless using `fill_with_none=True`. |
| `fill_with_none` | `bool`   | If `True`, fills with `None` when `new_values` is shorter. If `False` and lengths mismatch, throws an error. |

---

### Usage Example

```python
# Imports 
from Gen import colors as gcolor
from Classes.persona_class import Persona
from Base.tabla_builder import Table
import polars as pl
from rich import print

# Generate a list of fake people
list_of_persona = []

for i in range(25):
    p = Persona(i)
    list_of_persona.append(p.to_dict())  # use to_dict() to later pass it to the table

# Create a table from the list of people
table_example = Table("People")
table_example.add_dict(list_of_persona)

# Generate a list of favorite colors (can be longer or shorter than people list)
favorite_colors = gcolor.gen_colors(35, language="Es")

# Add the column 'Favorite Color' to the table, allowing filling with None if not enough values
table_example.add_list_as_column(
    table_index=0,
    colname="Favorite Color",
    new_values=favorite_colors,
    fill_with_none=True
)

# Show the result
print(table_example.dict_list)
```
## Example of the `add_options_as_column()` Method

This example shows how to add columns with predefined options to a table built from `Persona` objects.  
Each row in the table will receive a random value selected from the provided list.  
We use `Persona` here, but you can use any object (or no object at all) to create the table as shown in previous examples.

---

###   Quick Method Description

```python
add_options_as_column(
    table_index: int,
    colname: str,
    options: list
)
```

- `table_index`: Index of the table in `dict_list`.
- `colname`: Name of the new column.
- `options`: A list of values from which one will be randomly assigned to each row.

---

###  Usage Example

```python
from Classes.persona_class import Persona
from Base.tabla_builder import Table
import polars as pl

# Generate a list of Persona objects
list_of_persona = []

for i in range(25):
    p = Persona(i)
    list_of_persona.append(p.to_dict())

# Create a table from the list
table_example = Table("People")
table_example.add_dict(list_of_persona)

# Add a "strengths" column with one random option per row
table_example.add_options_as_column(
    0,
    "What are your strengths?",
    ["Adaptability", "Creativity", "Team-Work", "Resilience"]
)

# Add a question column with yes/no/neutral options
table_example.add_options_as_column(
    0,
    "Are you happy in your current job?",
    [True, False, "I don't care"]
)

# Show result
print(table_example.dict_list)
```
## Example of the `to_df()` Method

The `to_df()` method converts a list of dictionaries into a `DataFrame`.

---

### Parameters

| Parameter      | Type   | Description                                                                 |
|----------------|--------|-----------------------------------------------------------------------------|
| `table_index`  | `int`  | Index of the table inside `self.dict_list` you want to convert to a DataFrame. |

---

###  Usage Example

```python
from Base.tabla_builder import Table
import polars as pl
from rich import print

# Create the table
table_ex = Table("Example table")

# Add fake people data using Persona class
table_ex.add_persona_data_table(5)

# Convert the table at index 0 to a DataFrame
table_ex.to_df(0)

# Show the result
print(table_ex.dfs[0])
```
## Example of the `export_tables_to_csv()` Method

This method exports all `DataFrames` stored in the `self.dfs` attribute to CSV files.  
Each `DataFrame` is saved with a name that includes the given prefix and its index number.

---

### Parameters

| Parameter   | Type   | Description                                            |
|-------------|--------|--------------------------------------------------------|
| `filename`  | `str`  | Base prefix for the name of each CSV file to generate. |

---

### What does this method do?

- Takes all `DataFrames` from the `self.dfs` list.
- Exports them as individual CSV files.
- Files are named as:  
  `"{filename}_1.csv"`, `"{filename}_2.csv"`, etc.

---

### 💡 Usage Example

```python
# Assuming you have already converted tables to DataFrames
table_example.export_tables_to_csv("People") 
# This generates: People_1.csv, People_2.csv, etc.
```
## Example of the `add_persona_data_table()` Method

This method generates a table with fake person data using the `Persona` class, and adds it to `dict_list`.

---

### Parameters

| Parameter  | Type  | Description                                          |
|------------|-------|------------------------------------------------------|
| `size`     | `int` | Number of persons (`Persona` instances) to generate. |

---

### What does this method do?

- Creates a list of dictionaries generated from `Persona` objects.
- Adds that list as a new table to `self.dict_list`.
- Prints to console the index (`index`) where the new table was saved.

---

### 💡 Usage Example

```python
table_ex = Table("People")

table_ex.add_persona_data_table(10)

# Output: Persona table created! in 'dict_list' index → 0
```
