# DATA GENERATOR 1.0

- [ESPAÑOL](README_es.md)
- [ENGLISH](README.md)

**Data Generator** es una herramienta para generar datos mezclando datos reales y falsos. Ideal para crear:

- Datos de prueba (.csv, .parquet).
- Entrenamiento de modelos de Machine Learning.
- Bases de datos falsas.
- Tutoriales de enseñanza de programación.
- Simulaciones de sistemas.
- Analisis de Datos.
- Portafolio Dashboards para PowerBi.
- Practicar ETL.
- Data Science.


---
## Índice
- [Tipos de Generadores](#tipos-de-generadores)
  - [📒 Gen (Módulos)](#módulos)
  - [📕 Classes (Clases)](#clases)
  - [📙 Bases (Constructores de Tabla)](#bases)
---

---

## Indicaciones

**Fake Data Generator** es una herramienta que ofrece funciones y clases para generar tus propios datasets.  
Es importante entender que se importa y comport de diferentes maneras según el tipo de generador que se esté utilizando , ya que decidí separar a los generadores por niveles 

- generadores que generan solo listas **Gen** los llame modulos de gen.
- generadores que generan mas de un dato **Classes** los llame modulos de classes que es una clase con atributos y metodos.

A continuación, se detallan los tipos de generadores y su representación visual:

### Tipos de Generadores

| Tipo de Generador | Descripción                                                                                                                                                                                                                                                                               | Representación |
|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|
| `Gen`             | Módulo generador básico. Contiene archivos `.py` con funciones que devuelven arrays aleatorios del tema seleccionado. Permite configurar el rango y longitud de los resultados. <br>**Nota:** Si deseas que los datos no se repitan, debes establecer el parámetro `repeat=False`.         | 📒             |
| `Classes`         | Carpeta con generadores de tipo dos. En lugar de un solo dato, retornan estructuras más completas (como si fueran tablas), incluyendo múltiples campos extra (algunos con hasta 20). Se usan importando la clase y creando instancias, con docstrings que explican su funcionalidad.         | 📕             |
| `Bases`           | Contiene el módulo `Table Builder`, que permite convertir `DataFrames` en archivos `.csv`. Esto facilita el análisis y construcción de tablas personalizadas a partir de los datos generados.                                                                                              | 📙             |


## Módulos

Los módulos son archivos de Python ubicados en la carpeta `Gen`. Cada módulo contiene funciones especializadas para la generación de datos falsos. El nombre de cada archivo refleja el tipo de datos que genera. Como recomendación, intenta ser modular e importar solo los módulos que necesites, utilizando un alias adecuado para mantener el código limpio y eficiente. A continuación, se presenta el índice de los módulos disponibles en la carpeta `Gen`. Aunque es solo una recomendacion puedes importar todo `Gen` y de igual forma usar los modulos.

### se pueden eliminar Modulos inecesarios?

Sí la idea de tener archivos `.py` separados en `Gen` es que puedes eliminar los archivos y modulos que no uses , si bien puedes eliminar modulos , algunos modulos son importante no eliminarlos , ya que se usan para otros modulos y clases , si aun decides quitarlos revisa la lista de modulos y como proceder a eliminarlos.

- [Revisar lista de modulos](listadearchivosborrar)

### Índice de Módulos

- [Módulo `name.py`](Documentation\Modules\lang\Es\name_es.md)
- [Módulo `country.py`](Documentation\Modules\lang\Es\country.md)
- [Módulo `colors.py`](Documentation\Modules\lang\Es\colors.md)
- [Módulo `company.py`](Documentation\Modules\lang\Es\company.md)
---

## Clases

Las clases son similares a los modulos de `Gen` , la diferencia esta en que los modulos de `Gen` generan un tipo dato , mientras que las clases , generan un objeto aleatorio , con distintos atributos y métodos. que pueden servirte para crear tablas y dataFrame de manera mas facil que con `Gen`. `Classes` es una manera de crear datos aleatorios que esta pensada para crear tablas y diccionarios mas rapidos .Las clases tienen un Atributo en donde contiene el `DataFrame` o un método `to_dict()` que retorna un dict con todos los atributos en forma de clave valore ,que luego puedes usar para convertir en `DataFrame`, la carpeta `Classes` contine generadores conocidas como `colors` ,`country` y `companies` etc.  


### se pueden eliminar Clases inecesarias?

Sí , aunque recomiendo de igual forma darle un vistazo a la lista de modulos y clases , ya que ciertos modulos usan alguna clase , eliminar la clase conlleva tambien eliminar ciertas funciones de los modulos o todo el modulo , si esta constuido sobre este.

- - [Revisar lista de modulos](/Documentation/Files.MD) # falta por hacer

### Índice de Módulos 
- [Módulo `Color class`](Documentation\Classes\lang\Es\color.md)
- [Módulo `Company class`](Documentation\Classes\lang\Es\Company.md)
- [Módulo `Country class`](Documentation\Classes\lang\Es\country.md)

---
## Bases

Dentro de Carpeta Base se incluye por el momento `tabla_builder.py` el cual es un modulo que sirve para importar el objeto `Table` que servira para crear tablas de datos y exportarlas en formato csv

### Se puede eliminar?

si  `table_builder.py` puede eliminarse por que no se usa dentro de `Classes` ni de `Gen`

### Índice 

[Módulo `Base`](Documentation/Bases/lang/Es/Table_Builder.md)