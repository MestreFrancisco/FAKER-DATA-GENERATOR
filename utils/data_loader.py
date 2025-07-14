import polars as pl 
import numpy as np

REPEAT=True
NO_REPEAT=False

def open_parquet(routh):
    """ Open parquets files an return a Data Frame """
    df=pl.read_parquet(routh)
    
    return df

def open_csv(routh):
    """ Open parquets files an return Data Frame """
    df = pl.read_csv(routh)
    
    return df

def open_txt(routh,size=1,repeat=REPEAT):
    """ Open txt files and return np.array """
    
    with open(routh, encoding="utf-8") as f:
        numpy_array = np.array([line.strip() for line in f if line.strip()]) #Crea un array de numpy que 
    
    try:
        array_with_selected_data = np.random.choice(numpy_array, size=size, replace=repeat) # Numpy ya te deja eleigr el size y si se repite o no
    except:
        return numpy_array
        
    return np.array(array_with_selected_data)

def open_txt2(routh):
    with open(routh, encoding="utf-8") as f:
        numpy_array = np.array([line.strip() for line in f if line.strip()])     
    
    return numpy_array
        
        

def chooser(size,arr1,arr2):
    
    arr1_idx = np.random.randint(0, arr1.size, size)
    arr2_idx = np.random.randint(0, arr2.size, size)

    names = arr1[arr1_idx]
    surnames = arr2[arr2_idx]

    return np.char.add(names, " " + surnames)


def chooser3(size,arr1,arr2,arr3):
    
    arr1_idx = np.random.randint(0, arr1.size, size)
    arr2_idx = np.random.randint(0, arr2.size, size)
    arr3_idx = np.random.randint(0, arr2.size, size)

    names = arr1[arr1_idx]
    surnames = arr2[arr2_idx]
    second_surnames = arr3[arr3_idx]

    return np.char.add(names, " " + surnames +" " + second_surnames)

#-Specifict function for countrys
def filter_country(Country):
    """filter by country parameter"""
    
    df = open_csv(f"Data/country/countrys_advanced.csv")
    try:
        country_lower = Country.lower()

        filtered_country = df.filter(
            (pl.col("En").str.to_lowercase() == country_lower) |
            (pl.col("Es").str.to_lowercase() == country_lower) |
            (pl.col("Cat").str.to_lowercase() == country_lower) |
            (pl.col("iso3").str.to_lowercase() == country_lower) |
            (pl.col("iso2").str.to_lowercase() == country_lower) |
            (pl.col("Fr").str.to_lowercase() == country_lower))

    except:
        print(Country ," Not exist or your write in the incorrect form")
        print(df.select(["En"]))
        return 0
        
    return filtered_country