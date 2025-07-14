# FILES

This document contains information about the contents of the `**Data**` folder.  
You can extend and add files if needed. It also explains what happens if you want to delete certain files.

## Index

- [📁 Colors](#colors)
- [📁 Country](#country)
  - [📁 provinces and cities country](#folder-provinces-and-cities-country)
- [📁 Names](#names)
  - [📁 Folder `people`](#folder-people)
  - [📁 Folder `companies`](#folder-companies)
  - [📁 Folder `extra`](#folder-extra)
- [❌ Deleting Files, Modules, Classes](#deleting-files-modules-classes)
  - [🆑 Delete `Data/Names/people`](#-delete-datanamespeople)
  - [🆑 Delete `Data/Names/companies`](#-delete-datanamescompanies)

---

## 📁 Colors

The `colors` folder contains a total of 14 files:
- 13 `.csv` files with color names.
- 1 `.parquet` file containing the name of all colors.

> #### Columns:
> - image_url  
> - Es  
> - En  
> - en_2  
> - hex_cod  
> - RGB  

To extend it, you can add more files with the same column structure and a unique filename.  
You can also expand the different color ranges inside the CSVs.  
If you want to add more columns, you must also update the `Color` class.  
Modifying the `.parquet` file is recommended to avoid editing all 13 CSVs individually.

---

## 📁 Country

The `country` folder contains:
- 1 subfolder named `provinces and cities country`
- 2 CSV files.

The two CSVs include country data. One contains a simple list, and the other contains additional data in column format.

### 📁 Folder `provinces and cities country`

- Contains 207 `.parquet` files.  

Each `.parquet` file is named after a country in lowercase and without accents (in Spanish).  
Each file contains information about that country’s provinces and cities.

---

## 📁 Names

Contains:

- 3 folders:

### 📁 Folder `people`:

Contains:
- 11 `.txt` files including:
> - Female and male first names  
> - Last names  

To extend the list, indicate if the file is `male` or `female` and add a `_` followed by the region. For example:

- `male_south_america.txt`  
- `female_french.txt`

### 📁 Folder `companies`:

Contains:

- 10 `.txt` files

To extend it, follow the same naming pattern used in the existing files.

### 📁 Folder `extra`:

Currently empty.

You can create your own name datasets here using any rules you want.

---

## Deleting Files, Modules, Classes?

To delete files and folders you don't want to use, keep in mind that generator functions rely on these files.  
Below is a guide on what else must be deleted if you remove something.

---

## Data/Name

### 🆑 Delete `Data/Names/people`:

- ❌ If you delete `Names/people` → delete `Gen/names.py`  
- ❌ If you delete `Gen/names.py` → delete `Classes/persona_class.py`  
- ❌ If you delete `persona_class.py` → ❌ The method `add_persona_data_table()` in `Base/tabla_builder` will raise an error.  
  You can still use the rest of the module normally by removing this function.

### 🆑 Delete `Data/Names/companies`:

- coming soon
