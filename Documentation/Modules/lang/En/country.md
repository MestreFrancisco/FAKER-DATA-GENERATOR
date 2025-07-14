# 📒 MODULE `country.py`

- Next module [📒 Module colors](colors.md)
- For more functions see [📕 Country Class](../../../Classes/lang/En/country.md)
- Back to Readme [Fake Data Generator](../../../../README.md)

This module allows generating information about countries, including:

- Country names in different languages (with a total of 246 countries available to generate).
- ISO codes of countries, both in `iso2` and `iso3` formats.

---

### Available Functions

| Function                         | Description                                                                                      |
|---------------------------------|--------------------------------------------------------------------------------------------------|
| `gen_countrys()`                | Generates country names according to the language specified as a parameter.                      |
| `gen_cod_iso_country()`          | Generates ISO codes of countries. You can choose between `iso2` or `iso3` depending on the parameter. |
| `gen_all_countries_objects()`   | Generates an array of `Country()` objects, with all countries available in the CSV.              |
| **More functions available**     | Coming soon. You can share your ideas for new functions.                                        |

---

### Common Parameters

- **`size`**: Number of countries to generate.
- **`repeat`**: 
  - `True`: Allows countries to repeat.
  - `False`: Ensures unique countries are generated. **IF** the size requested is greater than 246, it returns 0 and an error.
- **`language`**: Language in which country names will be generated. Valid values are:
  - `"Es"`: Spanish → ❗**recommended for some functions**.
  - `"Fr"`: French
  - `"Cat"`: Catalan
  - `"En"`: English → ❗**recommended for some functions**.
  - Other languages may be added in the future.
- **`iso`**: Type of ISO code to generate:
  - `"iso2"`: 2-character ISO code (e.g., "AR" for Argentina).
  - `"iso3"`: 3-character ISO code (e.g., "ARG" for Argentina).

### Usage Examples

```python
# Import the Gen Country module as gc
from Gen import country as gc

# Generate 10 unique countries in Spanish
countries = gc.gen_countrys(size=10, repeat=False, language="Es")
print(countries)

# Generate 10 unique countries in French
countries = gc.gen_countrys(size=10, repeat=False, language="Fr")
print(countries)

#-------------------------------------------

# Generate 10 unique countries with ISO2 codes
countries = gc.gen_cod_iso_country(size=10, repeat=False, iso="iso2")
print(countries)

# Generate 10 unique countries with ISO3 codes
countries = gc.gen_cod_iso_country(size=10, repeat=False, iso="iso3")
print(countries)
