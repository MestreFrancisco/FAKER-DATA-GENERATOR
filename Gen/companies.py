from utils.data_loader import open_txt2,REPEAT,NO_REPEAT;
from random import choice as randomchoise
from numpy import array as nparray
from numpy import random as nrd
from itertools import product as itertoolsProduct
from Classes.company_class import Company

__FILE_ROUTH = f"Data/names/companies"


def gen_name(size=1,repeat=REPEAT,language="En"):
    """
    Generates a list of fake company names using prefixes and words.

    Parameters:
        size (int): Number of names to generate.
        repeat (bool): If True, allows repeated combinations.
        language (str): Language of the dataset. Only 'en', 'es' are supported you can add more!.

    Returns:
        list: A list of generated company names.
    """
    if language.lower() not in {"en", "es"}:
        raise ValueError(f"Invalid language '{language}'. Only 'En' and 'Es' are supported.")
    
    else:
        prefix = open_txt2(__FILE_ROUTH + f"/prefix_{language.lower()}.txt");
        word = open_txt2(__FILE_ROUTH + f"/words_{language.lower()}.txt");
    companies_names = [];
    if repeat==REPEAT: 
        for _ in range(size):
            p=randomchoise(prefix);
            w=randomchoise(word);
            companies_names.append(p +" "+ w);
        
        return companies_names;    
    if repeat==False:        
        if prefix.size * word.size  < size:     
           raise ValueError(f"📢 The max of unique values are {prefix.size * word.size} add more values or change the size")
        
        else:
            all_combinations = nparray([p +" "+ w for p , w in itertoolsProduct(prefix, word)])
            nrd.shuffle(all_combinations)
            fake_names = all_combinations[:size]
            return fake_names
            
            
def gen_obj_Company(size, repeat=REPEAT, language="En",size_company="all"):
    """
    This function generates Company objects.

    Recommendations
    ---
    - If you create more than 500 objects, the function will not fill all data automatically, 
    as it may take too much time.
    - If you want to change this behavior, modify the function or create a separate loop to 
    handle each object individually.

     Attributes
    ---
    - size(int) → Number of companies to generate (if > 500, data filling is disabled).
    - repeat(bool) → Defaults to True (allows repeated company names).
    - language(str) → Language for company names. Options: "spanish" or "english". Defaults to "english".
    """

    
    ListofName = gen_name(size, repeat, language)

    categorias = [
        "Technology", "Finance", "Healthcare", "Education", "Retail",
        "Real Estate", "Energy", "Transportation", "Hospitality",
        "Manufacturing", "Telecommunications", "Entertainment",
        "Agriculture", "Automotive", "Construction", "Aerospace",
        "Logistics", "Food & Beverage", "Legal Services", "Nonprofit"
    ]
    tamaños = ["micro", "small", "medium", "large", "extra", "global"]

    random_sizes = [randomchoise(tamaños) for _ in range(size)]
    random_categories = [randomchoise(categorias) for _ in range(size)]

    listofObj = []
    for i in range(size):
        company_obj = Company(ListofName[i], random_categories[i], random_sizes[i], i + 1)
        if size <= 500:
            company_obj.fill_all_values()
        listofObj.append(company_obj)

    return listofObj  # ← Solo retorna los objetos