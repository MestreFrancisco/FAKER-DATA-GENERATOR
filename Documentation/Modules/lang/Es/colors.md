# 📒 MÓDULO `colors.py`

- Regresar Readme [Fake Data Generator](../../../../README_es.md)
- Modulo siguiente [📒 Modulo company](company.md)

    El módulo `Colors` permite generar colores en diferentes formatos de manera organizada.  
---
Este módulo proporciona funciones para generar colores en distintos formatos y estilos:

- Nombres de colores basados en un dataset de Wikipedia (833 colores)  
- Colores aleatorios en formato hexadecimal  
- Colores aleatorios en formato RGB  
- Matrices 2D de colores hexadecimales  
- Colores clásicos hexadecimales específicos (negro, blanco, rojo, azul, verde, amarillo)  


## Funciones principales

### Funcion Generadora de nombre
Esta funcion retorna un array de nombres de colores aleatorios. usando un data set de wikipedia con un total de 833 colores con nombres , Instancia el objeto Color si quieres ver mas atributos de este dataSet.

| Función                | Descripción                            |
|------------------------|----------------------------------------|
| `gen_colors()`         |Genera un array de nombre de colores    |

#### 🟡 Parametros unicos
- `gamma="all"`  → Permite elegir la gamma de colores o el rango de colores , ve la lista completa en Data/Colors
- `language="En"` → Permite elegir el lenguaje solo hay dos Es y En , cualquier otro dara err

### Funciones Generadoras de  Codigos de Colores 
Estas Funciones generan codigos de colores hexadecimales y RGB , con estos generadores puedes generar todas las combinaciones de colores posibles , y tambien generar arrays de un solo color para crear imagenes. coloreando pixel por pixel , o para distintas cosas

-  Crear paletas de colores únicas o aleatorias.
-  Generar imágenes píxel por píxel a partir de matrices de color.
-  Visualizar datos y construir gráficos o interfaces interactivas.
-  Generar datos sintéticos para pruebas de procesamiento de imágenes o aprendizaje automático.
-  Rellenar zonas con colores fijos o uniformes.

| Función                   | Descripción breve                                                  |
|---------------------------|--------------------------------------------------------------------|
| `gen_random_hexcolor`     | Genera una lista de colores hex aleatorios.                        |
| `gen_rgb`                 | Genera una lista de colores en formato RGB.                        |
| `gen_hex_matrix`          | Genera una matriz 2D de colores hex.                               |
| `gen_hex_specific_color`  | Genera un arreglo con un solo color hex especificado.              |
| `gen_black`               | Genera un arreglo con el color negro clásico (`#000000`).          |
| `gen_white`               | Genera un arreglo con el color blanco clásico (`#FFFFFF`).         |
| `gen_red_basic`           | Genera un arreglo con rojo clásico (`#FF0000`).                    |
| `gen_blue_basic`          | Genera un arreglo con azul clásico (`#0000FF`).                    |
| `gen_green_basic`         | Genera un arreglo con verde clásico (`#00FF00`).                   |
| `gen_yellow_basic`        | Genera un arreglo con amarillo clásico (`#FFFF00`).                |
| `gen_red`                 | Genera un rojo más suave y moderno (`#AF2323`).                    |
| `gen_blue`                | Genera un azul más suave (`#2271B3`).                              |
| `gen_green`               | Genera un verde más moderno (`#009D71`).                           |
| `gen_yellow`              | Genera un amarillo más cálido (`#E9BD15`).                         |

---

## 💡 Ejemplos de uso

```python
from Gen import color as gcolor 

# 1. Generar 10 colores hex aleatorios
colors = gcolor.gen_random_hexcolor(size=10)

# 2. Crear una matriz de 5x5 con colores únicos
matrix = gcolor.gen_hex_matrix(5, 5, repeat=False)

# 3. Generar 100 colores RGB
rgb_array = gcolor.gen_rgb(size=100)

# 4. Rellenar una imagen con color verde mejorado
green_pixels = gcolor.gen_green(size=10000)
```


