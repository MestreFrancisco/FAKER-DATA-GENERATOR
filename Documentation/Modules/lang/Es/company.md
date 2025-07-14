# 📒 Modulo `Companies.py`:

El modulo `companies.py` es un generador que genera nombres de empresas ficticias en español e ingles por el momento.
- Regresar Readme [Fake Data Generator](../../../../README_es.md)

## gen_name

Genera una lista de nombres de empresas falsos combinando prefijos y palabras según el idioma seleccionado.

### Parámetros

| Parámetro   | Tipo     | Descripción                                                                 |
|-------------|----------|-----------------------------------------------------------------------------|
| `size`      | `int`    | Número de nombres a generar.                                                |
| `repeat`    | `bool`   | Si es `True`, permite combinaciones repetidas. Si es `False`, genera únicos.|
| `language`  | `str`    | Idioma del archivo base. Valores aceptados: `"En"` o `"Es"`.                |

### Retorna

- `list[str]`: Lista de nombres de empresa generados.

---

## gen_obj_Company
Genera objetos `Company` con nombres falsos, industria, tamaño, y ID. Si el tamaño es menor o igual a 500, se rellenan automáticamente los atributos extra de la empresa.

### Parámetros

| Parámetro   | Tipo     | Descripción                                                                 |
|-------------|----------|-----------------------------------------------------------------------------|
| `size`      | `int`    | Número de objetos `Company` a generar.                                      |
| `repeat`    | `bool`   | Si es `True`, permite repetir nombres. Si es `False`, serán únicos.         |
| `language`  | `str`    | Idioma del nombre de la empresa. `"En"` o `"Es"` (por defecto `"En"`).      |

### Retorna

- `list[Company]`: Lista de objetos `Company` generados con datos aleatorios.


## Ejemplo

```python
from Gen import companies as gcomp

#gen 100 companyes names for default options
names = gcomp.gen_name(100)
print(names)

#Company name gen 50 in Spanish that is not repeated
names = gcomp.gen_name(50,repeat=False,language="Es")
print(names)

#Gen 5 objects companies
list_of_obj_companies = gcomp.gen_obj_Company(size=100,language="Es") 
print(list_of_obj_companies)
```
cuando uses gcomp.gen_obj_Company() si imprimes mas de 500 objetos , solo se creara el obj en estado base , puedes usar el metodo a mano o cambiarlo en la definicion de la funcion. 