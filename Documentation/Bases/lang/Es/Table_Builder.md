# 📙 Base Table Builder

Table Builder esta pensada para que puedas crear tus propios dataFrames con todos los generadores y cosas que incluye este proyecto , y con las cosas que tu decidas tambien, ya que table builder tiene distintas funciones para hacer esto posible. Una vez crees y tengas tu tabla con el modulo Table Builder , puedes crear. el archivo csv , que exportara todas las tablas que hayas creado dentro del objeto `Table`. El objeto table tiene su forma de ser trabajado motivo por el cual se trato de darle la mejor explicacíon en los readme. Puedes consultar el indice para ir directo a un tema que te interese.

- Regresar Readme [Fake Data Generator](../../../../README_es.md)

## Indice
- [📙 Base Table Builder](#-base-table-builder)
- [Atributos](#atributos)
- [Funcionamiento](#funcionamiento)
  - [dict_list](#dict_list)
  - [dfs](#dfs)
- [Ejemplo rápido](#ejemplo-rapido)
- 🥟 [Ejemplo del Método `add_list_as_column()`](#ejemplo-del-método-add_list_as_column)
  - [Parámetros del Método](#-parámetros-del-método)
  - [Ejemplo de uso](#-ejemplo-de-uso)
- 🥟 [Ejemplo del Método `add_options_as_column()`](#ejemplo-del-método-add_options_as_column)
  - [Descripción rápida del método](#--descripción-rápida-del-método)
  - [Ejemplo de uso](#ejemplo-de-uso)
- 🥟 [Ejemplo del Método `to_df()`](#ejemplo-del-método-to_df)
  - [Parámetros](#parámetros)
  - [Ejemplo de uso](#ejemplo-de-uso)
- 🥟 [Ejemplo del Método `export_tables_to_csv()`](#ejemplo-del-método-export_tables_to_csv)
  - [Parámetros](#-parámetros)
  - [Ejemplo de uso](#-ejemplo-de-uso)
- 🥟 [Ejemplo del Método `add_persona_data_table()`](#ejemplo-del-método-add_persona_data_table)
  - [Parámetros](#-parámetros)
  - [Ejemplo de uso](#-ejemplo-de-uso)


## Atributos

| Atributo       | Tipo    | Descripción                                                             |
|----------------|---------|-------------------------------------------------------------------------|
| `tableName`    | `str`   | Nombre que identifica la tabla.                                         |
| `dict_list`    | `list`  | Lista vacía que almacenará datos en formato de diccionarios (tipo fila).|
| `dfs`          | `list`  | Lista vacía para almacenar objetos `DataFrame` (p. ej., páginas).       |

No se inicializan los atributos `dfs` y `dict_list` ya que estos se rellenan con los métodos que tiene table builder.

```python
from Base.tabla_builder import Table
import polars as pl

table_ex = Table("Example table")
```

[Ejemplo Rapido](#ejemplo_rapido)

## Funcionamiento

`Table` internamente contiene:

- `dict_list`: Una lista de listas de diccionarios, donde cada lista representa una ""tabla"" (como una colección de diccionarios) esto sirve para trabajar , ya sea modificaciones o añadiendo columnas extras a estos diccionarios y tabajar con estas tablas de forma independiente. estas se acceden mediante indices.

```python
from Base.tabla_builder import Table
import polars as pl
from rich import print


table_ex = Table("Example table")

dict_list = [{"Nombre":"Francisco",
            "Age":22}]

table_ex.add_dict(dict_list)

print(table_ex.dict_list[0])
```


- `dfs`: Una lista de objetos DataFrames. para llenar esta lista debes usar el metodo [`to_df`](#ejemplo-del-método--to_df)  

Esta función es especialmente útil cuando deseas agregar nuevos atributos a tus datos generados, como por ejemplo género, colores favoritos, salarios, etc.

## Ejemplo rapido
```python
from Base.tabla_builder import Table
from Gen import companies as gcomp
from rich import print

company = gcomp.gen_obj_Company(1)[0]
employes = company.employee_count

my_table = Table("my_first_table") # Creating table

my_table.add_persona_data_table(employes) # adding employes
my_table.add_dict(company.to_dict()) # adding company

print(my_table.dict_list)
```

```python

    {
            'id': 1,
            'name': np.str_('Sabrina Quintero Zapata'),
            'country': np.str_('Bahamas'),
            'age': 33,
            'mailcontact': 'sabrinaquinterozapata584@gmail.com'
        }+32 More Data...
    ],
    {
        'best_place_to_work': False,
        'company_anual_budget': 63046.62000000001,
        'company_month_budget': 7005.180000000001,
        'company_value': '315.23K',
        'company_value_no_abbreviate': 315233.10000000003,
        'contact_email': 'greeneasyflow@falsegmail.com',
        'continent': 'Australia y Oceanía',
        'country': 'Vanuatu',
        'employee_count': 13,
         +↓12 more keys data
    }

```


## Ejemplo del Método `add_list_as_column()`

El método `add_list_as_column()` se utiliza para añadir una nueva columna a una tabla ya existente dentro de la clase `Table`.  
Este método toma un nombre de columna, una lista de nuevos valores y la asigna como si fuera una nueva columna de datos a cada fila (diccionario) ya existente.

`Table` internamente contiene:

- `dict_list`: Una lista de listas, donde cada lista representa una tabla (como una colección de diccionarios).
- `tables`: Una lista de objetos DataFrame (por ejemplo, de Polars o Pandas).

Esta función es especialmente útil cuando deseas agregar nuevos atributos a tus datos generados, como por ejemplo género, colores favoritos, salarios, etc.

---

###  Parámetros del Método

| Parámetro         | Tipo     | Descripción                                                                                                                                      |
|-------------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| `table_index`     | `int`    | Índice de la tabla en `dict_list` a la que deseas añadir la nueva columna.                                                                     |
| `colname`         | `str`    | Nombre que tendrá la nueva columna. Este se usará como clave en cada diccionario de la tabla.                                                   |
| `new_values`      | `list`   | Lista de valores que se asignarán a la nueva columna. Debe tener la misma longitud que la tabla, a menos que se use `fill_with_none=True`.     |
| `fill_with_none`  | `bool`   | Si es `True`, rellenará con `None` en caso de que `new_values` sea más corta que la tabla. Si es `False` y hay diferencia de longitud, lanza error.|

---

### 💡 Ejemplo de uso

```python
# Importaciones 
from Gen import colors as gcolor
from Classes.persona_class import Persona
from Base.tabla_builder import Table
import polars as pl
from rich import print

# Generamos una lista de personas ficticias
list_of_persona = []

for i in range(25):
    p = Persona(i)
    list_of_persona.append(p.to_dict()) #usamos to dict para luego esto pasarlo como parametro a una tabla

# Creamos una tabla a partir de la lista de personas
table_example = Table("Personas")
table_example.add_dict(list_of_persona)

# Generamos una lista de colores favoritos (puede tener más o menos elementos que personas)
favorite_colors = gcolor.gen_colors(35, language="Es")

# Añadimos la columna 'Favorite Color' a la tabla, permitiendo completar con None si faltan valores
table_example.add_list_as_column(
    table_index=0,
    colname="Favorite Color",
    new_values=favorite_colors,
    fill_with_none=True
)

# Mostramos el resultado
print(table_example.dict_list)
```

## Ejemplo del Método `add_options_as_column()`

Este ejemplo muestra cómo añadir columnas con opciones predefinidas a una tabla construida a partir de objetos `Persona`. Cada fila de la tabla recibirá un valor aleatorio de la lista proporcionada. Se usa `Persona` en el ejemplo pero puedes usar cualquiero objeto o no para crear la tabla como ya aprendiste al inicio

---

###  Descripción rápida del método

```python
add_options_as_column(
    table_index: int,
    colname: str,
    options: list
)
```

- `table_index`: Índice de la tabla dentro de `dict_list`.
- `colname`: Nombre de la nueva columna.
- `options`: Lista de valores entre los cuales se seleccionará uno aleatorio para cada fila.

---

### Ejemplo de uso

```python
from Classes.persona_class import Persona
from Base.tabla_builder import Table
import polars as pl


list_of_persona = []

for i in range(25):
    p = Persona(i)
    list_of_persona.append(p.to_dict())

table_example = Table("Personas")
table_example.add_dict(list_of_persona)

table_example.add_options_as_column(
    0,
    "What are your strengths?",
    ["Adaptability", "Creativity", "Team-Work", "Resilience"]
)

table_example.add_options_as_column(
    0,
    "You are happy in your actual job?",
    [True, False, "I don't care"]
)

print(table_example.dict_list)
```
---

## Ejemplo del Método  `to_df()`

el método `to_df()` convierte en df una lista de diccionario pasado por parametro.

## Parámetros

| Parámetro       | Tipo   | Descripción                                                                 |
|-----------------|--------|-----------------------------------------------------------------------------|
| `table_index`   | `int`  | Índice de la tabla dentro de `self.dict_list` que se desea convertir a `DataFrame`. |


### Ejemplo de uso
```python
from Base.tabla_builder import Table
import polars as pl
from rich import print


table_ex = Table("Example table")

table_ex.add_persona_data_table(5)

table_ex.to_df(0)

print(table_ex.dfs[0])
```

## Ejemplo del Método `export_tables_to_csv()`

Este método exporta todos los `DataFrames` almacenados en el atributo `self.dfs` a archivos CSV.  
Cada `DataFrame` se guarda con un nombre que incluye el prefijo proporcionado y su número de índice.

---

###  Parámetros

| Parámetro   | Tipo     | Descripción                                                                 |
|-------------|----------|-----------------------------------------------------------------------------|
| `filename`  | `str`    | Prefijo base para el nombre de cada archivo CSV que se va a generar.        |

---

### ¿Qué hace este método?

- Toma todos los `DataFrames` de la lista `self.dfs`.
- Los exporta como archivos CSV individuales.
- Los archivos se nombran como:  
  `"{filename}_1.csv"`, `"{filename}_2.csv"`, etc.

---

###  Ejemplo de uso

```python
# Suponiendo que ya convertiste las tablas a DataFrames
table_example.export_tables_to_csv("Personas") 
# Esto genera: Personas_1.csv, Personas_2.csv, etc.
```

---

## Ejemplo del Método `add_persona_data_table()`

Este método genera una tabla con datos ficticios de personas utilizando la clase `Persona`, y la agrega a `dict_list`.

---

###  Parámetros

| Parámetro   | Tipo     | Descripción                                              |
|-------------|----------|----------------------------------------------------------|
| `size`      | `int`    | Número de personas (instancias de `Persona`) a generar.  |

---

###  ¿Qué hace este método?

- Crea una lista de diccionarios generados a partir de objetos `Persona`.
- Añade esa lista como una nueva tabla a `self.dict_list`.
- Muestra por consola el índice (`index`) donde fue guardada la nueva tabla.

---

###  Ejemplo de uso

```python
table_ex = Table("Personas")

table_ex.add_persona_data_table(10)

# Output: Persona table created! in 'dict_list' index → 0
```
