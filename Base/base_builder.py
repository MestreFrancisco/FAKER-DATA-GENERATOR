import sqlite3
import polars as pl
import pandas as pd
from rich.console import Console

console = Console()

class Base:
    
    def __init__(self,basename):
        
        self.conn = sqlite3.connect(basename)
        self.cursor = self.conn.cursor()
        console.print(f"sqlite DB created as name {basename}",style="Bold Green")
        
    # Create Table df
    def create_table_df(self,tablename:pl.DataFrame,df):
        """create a SQL table from a data frame"""
        pandadf = df.to_pandas()  # Convertir polars DataFrame a pandas
        pandadf.to_sql(name=tablename, con=self.conn, if_exists='replace', index=False)
        
        console.print(f"table {tablename} created ",style="blue")
        

    
    