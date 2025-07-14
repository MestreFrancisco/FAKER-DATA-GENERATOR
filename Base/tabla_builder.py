import polars as pl
import random 

class Table:
    
    
    def __init__(self,tablename):
        
        self.tableName = tablename
        self.dict_list = []
        self.dfs= []
    
    @staticmethod
    def convertToDf(dict_list):
        df=pl.DataFrame(dict_list)

        return df
    
    def add_dict(self,list_of_dicts):
        """
         Adds a new table represented as a list of dictionaries to the `dict_list` attribute.

         Each dictionary in the list represents a row (record), with keys acting as column names.

         Args:
            list_of_dicts (list): A list of dictionaries representing the data of a table.

         Example:
            [
                {"name": "Alice", "age": 30},
                {"name": "Bob", "age": 25}
            ]
        """    

        self.dict_list.append(list_of_dicts);

    def add_list_as_column(self, table_index, colname, new_values, fill_with_none=False):
        """
        Adds a new column to a table (list of dicts). 
        If lengths don't match, you can fill missing values with None if fill_with_none=True.
        """
        table = self.dict_list[table_index]

        # Si los tamaños no coinciden y no se permite rellenar, lanzar error
        if not fill_with_none and len(table) != len(new_values):
            raise ValueError("The length of the data does not match the number of rows , change fill_whith_none to True , to fill values if you wanna none values.")
        
    
        # Rellenar con datos o con None si se permiten rellenos
        for i, row in enumerate(table):
            if i < len(new_values):
                row[colname] = new_values[i]
            else:
                row[colname] = None
            
    def add_options_as_column(self, table_index, colname, options):
        """
        Adds a new column to a table by assigning random values from a given list of options.
        
        Parameters:
            table_index (int): Index of the table in self.dict_list to modify.
            colname (str): Name of the new column to add.
            options (list): List of possible values to randomly assign to the new column.
        
        Example:
            options = [True, False,"no value"]
            add_options_as_column(0, 'Accepted', options)
        """
        table = self.dict_list[table_index]
        
        for row in table:
            row[colname] = random.choice(options)
    
    def to_df(self,table_index):
        
         table = self.dict_list[table_index]
         
         df=pl.DataFrame(table)
         
         self.dfs.append(df)
         
    
    def export_tables_to_csv(self,filename):

        lista_de_dfs = self.dfs
        
        for i, df in enumerate(lista_de_dfs, start=1):
            df.write_csv(f"{filename}_{i}.csv")
            

    #---------------------Info Extra
    
    def add_persona_data_table(self,size):
        from Classes.persona_class import Persona
        
        list_of_p=[]
        
        for i in range(size):
            p = Persona(i)

            list_of_p.append(p.to_dict())
        
        self.dict_list.append(list_of_p)
        index = len(self.dict_list)-1 
        
        print("Persona table created! in 'dict_list' index → ",index)
            