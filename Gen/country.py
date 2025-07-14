from utils.data_loader import open_csv,REPEAT,NO_REPEAT
from numpy import random as rnd
import os

def gen_countrys(size=1 , repeat=REPEAT,language="En"):
    """ Generates a list of random country names from a CSV file.

    Parameters
    ----------
    size : int, optional
        Number of countries to return. Default is 1.
    repeat : bool, optional
        If True, allows repeated country names in the selection (sampling with replacement).
    language : str, optional
        Language of the country names. Must match a column in the CSV options are ("Es","En","Fr","Cat")

    Returns
    -------
    list
        A list of randomly selected country names.

    Raises
    ------
    FileNotFoundError
        If the CSV file is not found.
    KeyError
        If the specified language does not exist as a column in the CSV.
    ValueError
        If the requested number of unique countries exceeds the available ones when repeat is False.
    """

    try:
        df = open_csv("Data/country/countrys_advanced.csv")

        if language not in df.columns:
            raise KeyError(f"language '{language}' not founded in: {df.columns}")

        arr = df.select([language])[language].to_list()

        if not repeat and size > len(arr):
            raise ValueError(f" change repeat to ´True´ to print → {size} elements .")

        return rnd.choice(arr, size=size, replace=repeat)

    except FileNotFoundError:
        print("⚠️ Archivo CSV no encontrado.")
    except KeyError as e:
        print(f"⚠️  {e}")
    except ValueError as e:
        print(f"⚠️  {e}")
    return []
        

def gen_cod_iso_country(size=1 , repeat=REPEAT,iso="iso3"):
    """ Generates a list of iso code country names from a CSV file.

    Parameters
    ----------
    size : int, optional
        Number of countries to return. Default is 1.
    repeat : bool, optional
        If True, allows repeated country names in the selection (sampling with replacement).
    iso : str, optional
        Iso is a code for short the word country , the option are iso2 and iso3 for Default is iso3
        
        + iso2 → AR
        + iso3 → ARG
        
    Returns
    -------
    list
        A list of randomly iso code country names.

    Raises
    ------
    FileNotFoundError
        If the CSV file is not found.
    KeyError
        If the specified iso does not exist as a column in the CSV.
    ValueError
        If the requested number of unique countries exceeds the available ones when repeat is False.
    """

    try:
        df = open_csv("Data/country/countrys_advanced.csv")

        if iso not in df.columns:
            raise KeyError(f"iso '{iso}' not founded in: {df.columns}")

        arr = df.select([iso])[iso].to_list()

        if not repeat and size > len(arr):
            raise ValueError(f" change repeat to ´True´ to print → {size} elements .")

        return rnd.choice(arr, size=size, replace=repeat)

    except FileNotFoundError:
        print("⚠️ Archivo CSV no encontrado.")
    except KeyError as e:
        print(f"⚠️  {e}")
    except ValueError as e:
        print(f"⚠️  {e}")
    return []


def gen_all_countries_objects():
    """
    Generates a list of all Country objects.

    Warning
    -------
    This function is heavy and memory-intensive,
    as it loads all countries along with their provinces and cities
    using the Country() class.

    Returns
    -------
    list
        List of Country objects, one for each country available in the dataset.
    """    
    from Classes.country_class import Country

    paises = gen_countrys(size=246,repeat=False,language="En")
    country_obj_list = []
    
    for country in paises:
        name = country.lower()
        
        countryOBJ = Country(name,True) 
        country_obj_list.append(countryOBJ)
        
    return country_obj_list