# 📒 Module `Companies.py`:

The `companies.py` module is a generator that creates fake company names in Spanish and English for now.
- Back to Readme [Fake Data Generator](../../../../README.md)

## gen_name

Generates a list of fake company names by combining prefixes and words based on the selected language.

### Parameters

| Parameter   | Type     | Description                                                                |
|-------------|----------|-----------------------------------------------------------------------------|
| `size`      | `int`    | Number of names to generate.                                               |
| `repeat`    | `bool`   | If `True`, allows repeated combinations. If `False`, generates unique names.|
| `language`  | `str`    | Language of the base file. Accepted values: `"En"` or `"Es"`.              |

### Returns

- `list[str]`: List of generated company names.

---

## gen_obj_Company

Generates `Company` objects with fake names, industry, size, and ID. If the size is 500 or less, additional company attributes are automatically filled.

### Parameters

| Parameter   | Type     | Description                                                                 |
|-------------|----------|-----------------------------------------------------------------------------|
| `size`      | `int`    | Number of `Company` objects to generate.                                   |
| `repeat`    | `bool`   | If `True`, allows repeated names. If `False`, names will be unique.        |
| `language`  | `str`    | Language for company names. `"En"` or `"Es"` (default is `"En"`).           |

### Returns

- `list[Company]`: List of generated `Company` objects with random data.

---

## Example

```python
from Gen import companies as gcomp

# Generate 100 company names with default options
names = gcomp.gen_name(100)
print(names)

# Generate 50 unique company names in Spanish
names = gcomp.gen_name(50, repeat=False, language="Es")
print(names)

# Generate 100 Company objects in Spanish
list_of_obj_companies = gcomp.gen_obj_Company(size=100, language="Es") 
print(list_of_obj_companies)
