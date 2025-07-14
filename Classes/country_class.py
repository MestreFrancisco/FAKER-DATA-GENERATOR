from utils.data_loader import open_csv,open_parquet,filter_country
from polars import col as column

import os

FILE_ROUTH = os.path.join("Data", "country")
PROVINCES_PATH = f"Data/country/provinces_and_cities_countrys/"

class Country:
    """
    EN
    ---
    Represents a country with multilingual names, ISO codes, phone code, and continent.
    Also provides access to province-level data from a Parquet file (if available).

    Attributes:
        name (str): Country name in English.
        name_spanish (str): Country name in Spanish.
        name_french (str): Country name in French.
        name_catalan (str): Country name in Catalan.
        provinces_cities (dict → arr) null dict , use create_dict_whit_provinces_and_cities to fill it.
        phone_code (str): International phone code.
        provinces (arr): list of provinces
        iso2 (str): (e.g., 'BR').
        iso3 (str): (e.g., 'BRA').
        continent (str): Continent where the country is located.

    ES
    ---
    Representa un país con nombres en varios idiomas, códigos ISO, código telefónico y continente.
    También permite acceder a los datos de provincias desde un archivo Parquet, si están disponibles.
    """
    
    province_cities = {}
    
    def __init__(self,country,ignoreErrorMessage=False):
        
        self.table = filter_country(country)
     
     # ✅ Validación: evitar errores si no se encuentra el país
        
        if ignoreErrorMessage == True:
           pass
        else:
            if self.table.is_empty():
                raise ValueError(f"Country  " + country + " not founded. verify if country exist in csv file.")
      
        
     
        self.name = self.table.get_column("En")[0]
        self.name_spanish = self.table.get_column("Es")[0]
        self.name_french = self.table.get_column("Fr")[0]
        self.name_catalan = self.table.get_column("Cat")[0]
     
        self.phone_cod = self.table.get_column("phone_cod")[0]
     
        self.iso2 = self.table.get_column("iso2")[0]
        self.iso3 = self.table.get_column("iso3")[0]
     
        self.continet = self.table.get_column("continent")[0]
        try:
            self.provinces = self.__get_provinces().select(["province"])["province"].to_list()
        except:
            self.provinces = ["not data yet"]
     
    def __get_provinces_and_cities_dataset(self,ignoreErrorMessage=False): 
        try:
            nombre = self.name_spanish.lower();
            nombre = (
            nombre.replace("á", "a")
              .replace("é", "e")
              .replace("í", "i")
              .replace("ó", "o")
              .replace("ú", "u")
              .replace("ñ", "n")
              .replace(" ","_"));
            
            df = open_parquet(PROVINCES_PATH + f"{nombre}.parquet");
        except:
            #if ignoreErrorMessage == True
            #print("Verify in Data\country\provinces_and_cities_countrys ,if the country contain a  provinces file .parquet");
            pass
        
        return df;
          
    def __get_provinces(self):
        """EN: Fetch the list of provinces and return them as a polars DataFrame.\n ES:Obtiene la lista de provincias y la devuelve como un DataFrame."""
        try:
            df = self.__get_provinces_and_cities_dataset()
        except:
            return ["not data yet"]
        only_provinces = df.select([column("province").unique()])

        return only_provinces
          
   
    def __get_cities_of(self,province_name):
        
        df = self.__get_provinces_and_cities_dataset()
        try:
            filtered_df = df.filter(column("province") == province_name)
            cities = filtered_df.select(column("cities").unique())
            return cities
        except Exception as e:
            print("Error: Please make sure the province name matches exactly a value in the 'province' column.")
            print(f"Details: {e}")
            # Devolver un DataFrame vacío con la columna 'cities' para evitar errores posteriores
            return df.select(column("cities")).limit(0)
        
    def create_dict_whit_provinces_and_cities(self):
        """Alert! This function create a dict whit all provinces and cities"""
        
        dict = {};
        
        for province in self.provinces:
            
            dict[province] = self.__get_cities_of(province).select(["cities"])["cities"].to_list()
        
        self.province_cities = dict    