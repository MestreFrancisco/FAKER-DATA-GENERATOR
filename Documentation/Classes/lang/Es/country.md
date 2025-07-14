# 📕 Clase `Country`:

Con la clase `Country` podremos crear un objeto que contendrá información sobre un país, como su nombre, abreviaturas ISO, provincias y ciudades. A continuación se muestra un ejemplo de cómo importarla:

- Regresar Readme [Fake Data Generator](../../../../README_es.md)

```python
# Importar la clase Country
from Classes.country_class import Country

# Crear un objeto para un país específico
argentina = Country("Argentina")
```
el objeto Country cuenta con los siguientes Atributos

 ### **Atributos de Country**
---
| Atributo             | Descripción                                                                                                      |
|----------------------|------------------------------------------------------------------------------------------------------------------|
| `name`               | Retorna el nombre en inglés del país.                                                                            |
| `name_french`        | Retorna el nombre en francés del país.                                                                           |
| `name_spanish`       | Retorna el nombre en español del país.                                                                          |
| `name_catalan`       | Retorna el nombre en catalán del país.                                                                          |
| `phone_cod`          | Código de teléfono internacional del país (Ej. en Argentina es +54; si el país no tiene, se mostrará como +00). |
| `iso2` e `iso3`      | Abreviaturas ISO del país (Ej. 'AR', 'ARG').                                                                    |
| `continent`          | Continente donde se encuentra el país.                                                                          |
| `table`              | Muestra todos los datos del país.                                                                               |
| `provinces`          | Array de provincias del país. Si el país no tiene un archivo .parquet, el valor será ["no data yet"].            |
| `provinces_cities`   | Diccionario que, al llamar al método `create_dict_whit_provinces_and_cities`, cargará un array de arrays. Cada columna será una provincia con sus respectivas ciudades. <br> **❗ Nota Importante**: Si no tiene provincias, al llamar al método se generará un error. Para ver los archivos .parquet, revisa la ruta `Data\country\provinces_and_cities_countrys`. |

### **Métodos de Country**
---
| Método                               | Descripción                                                                                           |
|--------------------------------------|-------------------------------------------------------------------------------------------------------|
| `create_dict_whit_provinces_and_cities` | Este método toma el atributo `provinces_cities` y lo llena con las provincias del país y sus ciudades. Si no hay provincias, generará un error. Para ver los archivos .parquet, revisa la ruta `Data\country\provinces_and_cities_countrys`. |

## 📕 Lista de Classes

- [📕 Class Color](Color.md)
- [📕 Class Country](country.md)
- [📕 Class Company](Company.md)
- Regresar Readme [Fake Data Generator](../../../../README_es.md)