# FILES

En este Documento se encuentra informacion sobre que se encuentra en la carpeta `**Data**` . Puedes extender y agregar archivos si deseas. Ademas se explica tambien que pasa si queremos eliminar archivos.

## Indice 
- [📁 Colors](#-colors)
- [📁 Country](#-country)
  - [📁 provinces and cities country](#-carpeta-provinces-and-cities-country)
- [📁 Names](#-names)
  - [📁 Carpeta `people`](#-carpeta-people)
  - [📁 Carpeta `companies`](#-carpeta-companies)
  - [📁 Carpeta `extra`](#-carpeta-extra)
- [❌ Eliminar Archivos, Módulos, Clases](#eliminar-archivos--modulos--classes)
  - [🆑 Eliminar `Data/Names/people`](#-eliminar-datanamespeople)
  - [🆑 Eliminar `Data/Names/companies`](#-eliminar-datanamescompanies)

## 📁 Colors

En colors se encuentran un total de 14 Archivos
- 13 csv con nombres de colores.
- 1 archivo parquet con el nombre de todos los colores.
> #### Columnas:
> - image_url,
> - Es,
> - En
> - en_2
> - hex_cod
> - RGB

para extenderlo puedes agregar mas archivos cumpliendo con el mismo orden de columnas y colocar un nombre de archivo que no este , puedes tambien extender las diferentes gammas de colores dentro del csv. Si añades mas columnas deberas ir a modificar la clase Color . modifica el parquet para no tener que hacer esto en los 13 archivos.

## 📁 Country

Country contiene:
- 1 carpeta llamada provinces and cities country
- 2 archivos csv.

Los dos archivos csv contienen paises , en uno solo esta un listado y en otro hay mas datos en forma de columna.

#### 📁 Carpeta `provinces and cities country`

- Contiene 207 archivos parquet.

cada parquet se identifica con el nombre del pais en español sin acentos y en minisculas . cada parquet contiene info sobre las provincias y ciudades de dicho pais identificado como se menciono.

## 📁 Names

Contiene:

- 3 Carpetas

#### 📁 Carpeta `people`:

contiene:
- 11 elementos txt los cuales:
> - nombres femeninos y masculinos 
> - apellidos 

para extender nombres indica si es `male` o `female` añade un `_` seguido de la region ej:

- `male_south_america.txt`
- `female_frech.txt`

#### 📁 Carpeta `companies`:

Contiene:

- 10 archivos txt

para extenderlo sigue el mismo patron que con lo de nombres , mira los archivos veras que todos tienen un patron.

#### 📁 Carpeta `extra`:

Contiene: nada

puedes crear tus propios datos de nombre con reglas que tu quieras.


## Eliminar Archivos , Modulos , Classes?

Para eliminar los archivos y carpetas que no quieres usar debes tener en cuenta que las funciones de los generadores deben buscar estos archivos , acontinuacion te dejo la guia de que debes eliminar si deseas quitar algo.

## Data/Name

#### 🆑 Eliminar `Data/Names/people`:

- ❌ Sí eliminas Names/People → eliminar Gen/names.py 
- ❌ Sí eliminas Gen/names.py → eliminar Classes/persona_class.py.
- ❌ Sí eliminas Classes/persona_class.py → ❌ Dara error a la hora de llamar el método `add_persona_data_table()` del módulo `Base/tabla_builder` , puedes seguir usandolo con normalidad eliminando esta funcion.

#### 🆑 Eliminar `Data/Names/companies`:

- coming soon