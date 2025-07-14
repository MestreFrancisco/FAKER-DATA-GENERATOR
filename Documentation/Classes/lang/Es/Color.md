# 📕 Class `Color`:

La clase `Color` podreemos crear un objeto que servira para manipular una tabla mediante Polars o Pandas , preferiblemente polars. Este DateSet fue extraido de GitHub y Wikipedia revisa en Licencias y Menciones para informarte.

- Modulo siguiente [📕 class Country](country.md)
- Regresar Readme [Fake Data Generator](../../../../README_es.md)

### Atributos

| Atributo        | Tipo             | Descripción                                                                  |
|-----------------|------------------|------------------------------------------------------------------------------|
| `color_df`      | `DataFrame`      | DataFrame que contiene todos los colores. Usa `.head()` para mostrar una vista previa. |
| `colornames`    | `lista de str`     | Lista de nombres de colores en inglés.                                     |
| `colornames_es` | `lista de str`     | Lista de nombres de colores en español.                                    |
| `color_hex`     | `lista de str`     | Lista de códigos de color en formato hexadecimal.                          |
| `image_url`     | `lista de imagenes`| Lista de Url de imagenes donde se visualiza el color.                      |
| `rgb`           | `lista de int`     | Lista de valores RGB correspondientes a los colores.                       |

### Nota

Los atributos están sincronizados, lo que significa que puedes obtener la información de un color específico usando el mismo índice en todos los atributos.  
Por ejemplo, `colornames[0]`, `colornames_es[0]`, `color_hex[0]` y `rgb[0]` corresponden todos al mismo color.

## Ejemplo de uso

```python
# Importar la clase Color
from Classes.color import Color

colores = Color()

#Imprimir 10 nombres en español
print(colores.colornames_es[:10])

#Imprimir sus respectivos codigo hex
print(colores.color_hex[:10])

#Imprimir su url para visualizarlo
print(colores.image_url[:10])

```

## 📕 Lista de Classes

- [📕 Class Color](Color.md)
- [📕 Class Country](country.md)
- [📕 Class Company](Company.md)
- Regresar Readme [Fake Data Generator](../../../../README_es.md)

