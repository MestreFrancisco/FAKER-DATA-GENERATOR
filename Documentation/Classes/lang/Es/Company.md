# 📦 Clase Company

La clase `Company` es una herramienta de simulación que genera datos sintéticos de empresas, ideal para **dashboards y análisis en Power BI**. Sin embargo, su diseño modular permite utilizarla en cualquier proyecto que necesite estructuras empresariales simuladas, como pruebas, visualizaciones de datos, bases de datos ficticias o fines educativos.

Esta clase crea empresas con atributos aleatorios pero realistas, incluyendo número de empleados, presupuestos, niveles de satisfacción y distribución global, siendo perfecta para representar diferentes escenarios de negocio.

- Modulo siguiente [📕 class Persona](Persona.md)
- Regresar Readme [Fake Data Generator](../../../../README_es.md)

---

## Principales Atributos

| Atributo                          | Tipo     | Descripción                                                  |
|----------------------------------|----------|--------------------------------------------------------------|
| `id`                              | `int`    | Identificador único de la empresa.                           |
| `name`                            | `str`    | Nombre de la empresa.                                        |
| `industry`                        | `str`    | Industria o sector al que pertenece la empresa.              |
| `size_category`                   | `str`    | Categoría de tamaño (`micro`, `small`, `medium`, etc.).      |
| `employee_count`                 | `int`    | Número de empleados.                                         |
| `company_value`                  | `str`    | Valor total de la empresa en formato abreviado.              |
| `company_value_no_abbreviate`    | `float`  | Valor total de la empresa sin abreviar.                      |
| `country`                         | `str`    | País asignado a la empresa.                                  |
| `phone_number`                    | `str`    | Número de contacto internacional simulado.                   |
| `contact_email`                  | `str`    | Correo electrónico ficticio de contacto.                     |
| `open_projects`                 | `float`  | Número estimado de proyectos en curso.                       |
| `min_work_hour`                 | `int`    | Horas mínimas de trabajo diario.                             |
| `glassdoor_clasification`       | `float`  | Calificación simulada del ambiente laboral (1.0 a 5.0).      |
| `best_place_to_work`            | `bool`   | Indica si ha sido reconocida como “Mejor lugar para trabajar”. |
| `company_anual_budget`          | `float`  | Presupuesto anual estimado.                                  |
| `company_month_budget`          | `float`  | Presupuesto mensual estimado.                                |
| `salary_anual_budget_percentage`| `str`    | Porcentaje del presupuesto destinado a sueldos.              |
| `salary_anual_budget`           | `float`  | Gasto anual en salarios.                                     |
| `remote_friendly`               | `bool`   | Indica si permite trabajo remoto.                            |
| `hiring`                         | `bool`   | Indica si está contratando actualmente.                      |
| `employee_satisfaction`         | `str`    | Porcentaje de satisfacción laboral estimado.                 |

---

## Ejemplo de Uso

Puedes crear e imprimir una empresa así:

```python
from company_module import Company

empresa = Company("OpenAnalytics", "Software", "medium", 1)
empresa.print_info()
```

## Recomendaciones:

Recomiendo usar el modulo `companies.py`  y for , de todas maneras `companies.py` contiene una funcion que genera muchos objetos `Company` que serviran para crear tablas más adelantes , de esta manera puedes crear muchos objetos de manera aleatoria , mira el ejemplo en [Modulo Company](../../../Modules/lang/Es/company.md)


## 📕 Lista de Classes

- [📕 Class Color](Color.md)
- [📕 Class Country](country.md)
- [📕 Class Company](Company.md)
- Regresar Readme [Fake Data Generator](../../../../README_es.md)