# DATA GENERATOR 1.0

- [ESPAÑOL](README_es.md)
- [ENGLISH](README.md)

## Instructions
- Clone the Repo
```bash
git clone https://github.com/MestreFrancisco/FAKER-DATA-GENERATOR
```
- Install dependencys

```bash
pip install -r requirements.txt
```

you can start working , this use sqlite3


**Data Generator** is a tool for generating data by mixing real and fake data. Ideal for creating:

- Test data (.csv, .parquet)
- Machine Learning training datasets
- Fake databases
- Programming tutorials
- System simulations
- Data analysis
- Power BI portfolio dashboards
- ETL practice
- Data Science

---

## Index
- [Generator Types](#generator-types)
  - [📒 Gen (Modules)](#modules)
  - [📕 Classes](#classes)
  - [📙 Bases (Table Constructors)](#bases)
---

---

## Instructions

**Fake Data Generator** is a tool that offers functions and classes to generate your own datasets.  
It is important to understand that it behaves differently depending on the type of generator used, as generators are separated into levels:

- Generators that only return lists are grouped under **Gen** (modules).
- Generators that return more complex data (objects with multiple attributes) are grouped under **Classes**.

Below is a breakdown of generator types and their visual representation:

### Generator Types

| Generator Type | Description                                                                                                                                                                                                                                                                             | Icon |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------|
| `Gen`          | Basic generator module. Contains `.py` files with functions that return random arrays based on the selected topic. Allows you to set the range and length of the result. <br>**Note:** If you want the data to be unique, set `repeat=False`.                                          | 📒   |
| `Classes`      | Folder containing level-two generators. Instead of returning a single data item, they return more complete structures (like tables), including multiple extra fields (some with up to 20). Import the class and create instances. Each includes docstrings explaining functionality.     | 📕   |
| `Bases`        | Contains the `Table Builder` module, which allows you to convert `DataFrames` into `.csv` files. This makes it easy to build custom tables from generated data for export and analysis.                                                                                                 | 📙   |

## Modules

Modules are Python files located in the `Gen` folder. Each module contains specialized functions for generating specific types of fake data. The file name reflects the type of data it generates.  
For better organization, it's recommended to only import the modules you need using an alias — though importing everything is also supported.

### Can you delete unnecessary modules?

Yes. The reason for separating the `.py` files in `Gen` is to allow you to delete those you don't use.  
However, be cautious — some modules are dependencies for others or for certain classes.  
If you still want to remove something, review the list of modules and how to safely remove them.

- [Check removable modules list](listadearchivosborrar)

### Module Index

- [Module `name.py`](Documentation/Modules/lang/En/name_es.md)
- [Module `country.py`](Documentation/Modules/lang/En/country.md)
- [Module `colors.py`](Documentation/Modules/lang/En/colors.md)
- [Module `company.py`](Documentation/Modules/lang/En/company.md)

---

## Classes

Classes are similar to `Gen` modules. The main difference is that `Gen` modules generate a single type of data, while classes generate full objects with multiple attributes and methods.  
They are designed to help you generate tables and DataFrames faster.  
Each class includes a method like `to_dict()` that transforms its internal data into a dictionary format, which can then be used to create DataFrames.

The `Classes` folder includes generators such as `colors`, `country`, and `companies`, among others.

### Can you delete unnecessary classes?

Yes, but make sure to review the dependency list first.  
Some `Gen` modules depend on certain classes — deleting a class may require deleting a function or even an entire module that uses it.

- [Check removable modules list](/Documentation/Files_en.md) # to be completed

### Class Index

- [Module `Color class`](Documentation/Classes/lang/Es/color.md)
- [Module `Company class`](Documentation/Classes/lang/Es/Company.md)
- [Module `Country class`](Documentation/Classes/lang/Es/country.md)

---

## Bases

Inside the `Base` folder, you'll find `tabla_builder.py`, a module for importing the `Table` object.  
This is used to create and export custom data tables in `.csv` format.

### Can it be deleted?

Yes. `table_builder.py` can be safely deleted since it's not used by either `Classes` or `Gen`.

### Index

- [Module `Base`](Documentation/Bases/lang/En/Table_Builder.md)
