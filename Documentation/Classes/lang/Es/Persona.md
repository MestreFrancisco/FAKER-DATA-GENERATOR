# 📕 Class Persona

Class persona funciona como un super Gen de Nombres. La idea de class persona es que puedas generar directamente a personas con datos basicos como la `edad , nombre completo , apellido , mail e Id` , ademas sí deseas añadir mas columnas o datos para la persona, puedes crear tus propios métodos y atributos mediante herencia y modificaciones de la misma clase. 

- Modulo siguiente [📕 class Color](Color.md)
- Regresar Readme [Fake Data Generator](../../../../README_es.md)

## Atributos

| Atributo      | Descripción                                                       | Ejemplo                     |
|---------------|-------------------------------------------------------------------|-----------------------------|
| `id`          | Identificador único pasado por parametro (Obligatorio)            | 872                         |
| `name`        | Nombre completo generado aleatoriamente                           | Juan Pérez                   |
| `age`         | Edad generada según el rango definido por el parámetro `age` en el docstring     | 34           |
| `country`     | País seleccionado aleatoriamente de una lista                    | México                       |
| `mailcontact` | Correo electrónico generado a partir del nombre + número + dominio | juanperez123@gmail.com     |



## Métodos 

| Método       | Descripción                                                                                      | Retorno                         |
|--------------|--------------------------------------------------------------------------------------------------|----------------------------------|
| `to_dict()`  | Convierte los atributos definidos en la clase (`__slots__`) en un diccionario clave-valor.      | Diccionario con los datos de la persona, por ejemplo:<br>`{"id":6,"name": "Ana Ruiz", "age": 29, "country": "España", "mailcontact": "anaruiz87@gmail.com"}` |

## Ejemplo

```python
from Classes.persona_class import Persona
from rich import print
import polars as pl

p = Persona()

dict  = [p.to_dict()]

df = pl.DataFrame(dict)

print(df)

#Output
┌─────┬─────────────────────────┬─────────┬─────┬─────────────────────────────────┐
│ id  ┆ name                    ┆ country ┆ age ┆ mailcontact                     │
│ --- ┆ ---                     ┆ ---     ┆ --- ┆ ---                             │
│ i64 ┆ str                     ┆ str     ┆ i64 ┆ str                             │
╞═════╪═════════════════════════╪═════════╪═════╪═════════════════════════════════╡
│ 1   ┆ Charity Sanders Watkins ┆ France  ┆ 22  ┆ charitysanderswatkins954@gmail… │
└─────┴─────────────────────────┴─────────┴─────┴─────────────────────────────────┘
```

## 📕 Lista de Classes

- [📕 Class Color](Color.md)
- [📕 Class Country](country.md)
- [📕 Class Company](Company.md)
- Regresar Readme [Fake Data Generator](../../../../README_es.md)