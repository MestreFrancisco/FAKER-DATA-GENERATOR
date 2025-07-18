import Base.base_builder
import Base.tabla_builder
import polars as pl
import random


#Creando Objetos
mybase = Base.base_builder.Base("CurrencyGestionDB")
empleados = Base.tabla_builder.Table("empleados")

#Añadiendo info a personas
empleados.add_persona_data_table(50)
empleados.add_options_as_column(0,"Are you Working?",["Yes","Not"])
empleados.add_interger_range_as_columns(0,"Free time",2,6)
empleados.add_float_range_as_columns(0,"Salary",1_000.10,4_000.0)
empleados.add_options_as_column(0,"Currency",["USD","EUR"])
empleados.add_options_as_column(0,"I need to convert current currency into",["ARS","USD","MXN","CPL"])

empleados.to_df(table_index=0)
df = empleados.dfs[0]

mybase.create_table_df("Empleados",df)