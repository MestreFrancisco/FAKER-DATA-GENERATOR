# 📒 MODULE `names.py`

- Next module [📒 Module Country](country.md)  
- Back to Readme [Fake Data Generator](../../../../README.md)

This module allows you to generate:

- Male and female names  
- Region-specific names: `latam`, `north_america`, `asia`  
- Region-specific surnames  
- Full names: 1 first name + 2 last names  

---

### Available Functions `name`

| Function                 | Description                               |
|--------------------------|-------------------------------------------|
| `gen_male_name()`        | Generates male names                      |
| `gen_female_name()`      | Generates female names                    |
| `gen_surnames_region()`  | Generates surnames based on region        |
| `gen_names()`            | Generates names without gender distinction|
| `gen_surnames()`         | Generates general surnames                |
| `gen_full_name()`        | Generates full names: name + 2 surnames   |

---

### Common Parameters `name`

- `size`: Number of names to generate  
- `region`: Region of origin (`latam`, `north_america`, `asia`) – only for region-based functions  
- `repeat`: `True` allows repeated values, `False` ensures unique ones  

---

### Usage Examples `name`

```python
# Example: Using the name generators from Gen.names with alias `gname`

from Gen.names import name as gname

# 🔹 Generate 5 male names from Latin America
male_names = gname.gen_male_name(region="latam", size=5)
print("Male Names:", male_names)

# 🔹 Generate 3 female names from Asia
female_names = gname.gen_female_name(region="asia", size=3)
print("Female Names:", female_names)

# 🔹 Generate 4 surnames from North America
surnames_na = gname.gen_surnames_region(region="north_america", size=4)
print("Surnames (North America):", surnames_na)

# 🔹 Generate 6 general names (from names.txt)
names = gname.gen_names(size=6)
print("General Names:", names)

# 🔹 Generate 3 general surnames (from surnames.txt)
surnames = gname.gen_surnames(size=3)
print("General Surnames:", surnames)

# 🔹 Generate 5 full names (name + two surnames)
full_names = gname.gen_full_name(size=5)
print("Full Names:", full_names)
```