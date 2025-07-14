from Base.tabla_builder import Table
from Gen import companies as gcomp
from rich import print

# Generar 500 objetos Company
companies_number=500
company_data_list = gcomp.gen_obj_Company(companies_number)

# Convertir a lista de diccionarios
list_company_dicts = [company.to_dict() for company in company_data_list]

# Crear tabla
my_table = Table("my_table")

# Agregar la lista de diccionarios como una tabla
my_table.add_dict(list_company_dicts)

# Convertir a DataFrame la tabla (índice 0 porque es la primera)
my_table.to_df(0)

# Exportar a CSV
my_table.export_tables_to_csv("companies")

