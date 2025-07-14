# 📒 MÓDULO `country.py`

- Modulo siguiente [📒 Modulo colors](colors.md)
- Para más funciones ve a [📕 Clase Country](../../../Classes/lang/Es/country.md)
- Regresar Readme [Fake Data Generator](../../../../README_es.md)


Este módulo permite generar información sobre países, incluyendo:

- Nombres de países en diferentes idiomas (con un total de 246 países disponibles para generar).
- Códigos ISO de los países, tanto en formato `iso2` como `iso3`.

---

### Funciones Disponibles

| Función                              | Descripción                                                                                      |
|--------------------------------------|--------------------------------------------------------------------------------------------------|
| `gen_countrys()`                    | Genera nombres de países según el idioma especificado como parámetro.                           |
| `gen_cod_iso_country()`              | Genera el código ISO de los países. Puedes elegir entre `iso2` o `iso3` dependiendo del parámetro. |
| `gen_all_countries_objects()`       | Genera un array de objetos `Country()`, con todos los países disponibles en el CSV.              |
| **Más funciones disponibles**       | Están por venir. Puedes compartir tus ideas para nuevas funciones.                              |

---
### Parámetros Comunes

- **`size`**: Número de países a generar.
- **`repeat`**: 
  - `True`: Permite que los países se repitan.
  - `False`: Garantiza que los países generados sean únicos **SÍ** se pasa un size mayor a 246 retorna 0 y un error.
- **`language`**: Idioma en el que se generarán los nombres de los países. Los valores válidos son:
  - `"Es"`: Español → ❗**recomendado para ciertas funciones**.
  - `"Fr"`: Francés
  - `"Cat"`: Catalan
  - `"En"`: Ingles → ❗**recomendado para ciertas funciones**.
  - Otros idiomas pueden ser añadidos en el futuro.
- **`iso`**: Tipo de código ISO a generar:
  - `"iso2"`: Código ISO de 2 caracteres (Ejemplo: "AR" para Argentina).
  - `"iso3"`: Código ISO de 3 caracteres (Ejemplo: "ARG" para Argentina).

### Ejemplos de Uso

```python
# Importar el módulo Gen Country como gc
from Gen import country as gc

# Generar 10 países sin repetirse, en idioma español
paises = gc.gen_countrys(size=10, repeat=False, language="Es")
print(paises)

# Generar 10 países sin repetirse, en idioma francés
paises = gc.gen_countrys(size=10, repeat=False, language="Fr")
print(paises)

#-------------------------------------------

# Generar 10 países con código ISO2, sin repetirse
paises = gc.gen_cod_iso_country(size=10, repeat=False, iso="iso2")
print(paises)

# Generar 10 países con código ISO3, sin repetirse
paises = gc.gen_cod_iso_country(size=10, repeat=False, iso="iso3")
print(paises)

```
#### Generando todos los objetos de países: `gen_all_countries_objects()`

Este método genera un array de objetos `Country()`, cada uno representando un país con todos los atributos y métodos disponibles. Puedes utilizar estos objetos para acceder a información detallada de cada país.

```python
# Importar el módulo Gen Country como gc
from Gen import country as gcountry

# Generar un array con todos los objetos Country()
countrys_objects = gcountry.gen_all_countries_objects()

# Acceder al primer objeto del array
country = countrys_objects[0]

# Mostrar la tabla del objeto (información completa del país)
print(country.table)
```
#### El print mostraria esto

| Es    | En    | Cat  | Fr    | Continent | iso2 | iso3 | Phone Code |
|-------|-------|------|-------|-----------|------|------|------------|
| China | China | Xina | Chine | Asia      | CN   | CHN  | +238       |

por su puesto el primer elemento es random , este es solo un ejemplo , para ver mas datos , metodos y atributos del Objecto Country lea su funcion en [📕 Clase Country](/Documentation/Classes/lang/Es/country.md)
