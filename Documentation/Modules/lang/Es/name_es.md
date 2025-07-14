# 📒 MÓDULO `names.py`

- modulo siguiente [📒 Modulo Country](country.md)
- Regresar Readme [Fake Data Generator](../../../../README_es.md)

Este módulo permite generar:

- Nombres masculinos y femeninos
- Nombres por región: `latam`, `north_america`, `asia`
- Apellidos por región
- Nombres completos: 1 nombre + 2 apellidos

---

### Funciones Disponibles `name`

| Función                | Descripción                            |
|------------------------|----------------------------------------|
| `gen_male_name()`      | Genera nombres masculinos              |
| `gen_female_name()`    | Genera nombres femeninos               |
| `gen_surnames_region()`| Genera apellidos por región            |
| `gen_names()`          | Nombres sin distinción de género       |
| `gen_surnames()`       | Apellidos generales                    |
| `gen_full_name()`      | Nombre completo: nombre + 2 apellidos  |

---

### Parámetros Comunes `name`

- `size`: Número de nombres a generar
- `region`: Región de origen (`latam`, `north_america`, `asia`) – solo para funciones regionales
- `repeat`: `True` permite repetir nombres, `False` garantiza valores únicos

---

### Ejemplos de Uso `name`

```python
#Example: Using the name generators from Gen.names with alias `gname`

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