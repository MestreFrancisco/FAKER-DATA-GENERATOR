#  Clase Base para SQLite 

Esta clase `Base` facilita la creación y manejo de bases de datos SQLite, permitiendo crear tablas a partir de DataFrames, en particular usando `polars`. Además, incluye mensajes visuales con la librería `rich` para mejor interacción en consola.

---

## Atributos

| Atributo  | Tipo          | Descripción                                 |
|-----------|---------------|---------------------------------------------|
| `conn`    | `sqlite3.Connection` | Conexión a la base de datos SQLite.         |
| `cursor`  | `sqlite3.Cursor`     | Cursor para ejecutar comandos SQL.          |

---

## Métodos

### `__init__(self, basename)`

Inicializa la conexión a una base de datos SQLite con el nombre proporcionado.

| Parámetro | Tipo  | Descripción                        |
|-----------|-------|----------------------------------|
| `basename`| `str` | Nombre (o ruta) del archivo SQLite|

**Funcionamiento:**

- Establece conexión y cursor.
- Muestra mensaje de confirmación en consola usando `rich`.

---

### `create_table_df(self, tablename: str, df: pl.DataFrame)`

Crea una tabla en SQLite a partir de un DataFrame `polars`.

| Parámetro  | Tipo            | Descripción                                  |
|------------|-----------------|----------------------------------------------|
| `tablename`| `str`           | Nombre de la tabla a crear en SQLite.       |
| `df`       | `pl.DataFrame`  | DataFrame de Polars que se convertirá en tabla.|

**Funcionamiento:**

- Convierte el DataFrame de `polars` a `pandas` para usar el método `to_sql`.
- Crea o reemplaza la tabla en SQLite con el nombre dado.
- Muestra mensaje en consola confirmando la creación de la tabla.

---

## Ejemplo de uso

```python
from Base import Base
import polars as pl

# Crear instancia con nombre de base de datos
db = Base("mi_basedatos.sqlite")

# Crear un DataFrame polars de ejemplo
df = pl.DataFrame({
    "id": [1, 2, 3],
    "nombre": ["Ana", "Luis", "Carlos"]
})

# Crear tabla SQLite desde el DataFrame
db.create_table_df("personas", df)
