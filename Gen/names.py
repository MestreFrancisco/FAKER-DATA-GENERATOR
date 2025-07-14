from utils.data_loader import open_txt,chooser3,REPEAT,NO_REPEAT;
import os

__FILE_ROUTH = os.path.join("Data", "names", "people")


def gen_male_name(region="latam",size=1,repeat=REPEAT):
    
    """ Generate a male name from a specific region and return an array of type np.array.
        You can add your own data in the Data/names/people directory. The suffix **male_** is required for the file names.
    
        + _Parameters_:
        1. region → choose names based on region (latam,north_america,asia)
        2. size → size of array
        3. repeat → unique valors o not (change whit false or true)
        4. limit_array_on_length_error → si necesitas que de error cuando se pase del limite del array cambialo a False.
    """    
    region.lower()
    
    #Try catch to correct the errors
    try:
        routh = os.path.join(__FILE_ROUTH, f"male_{region}.txt")
    except Exception as e:
        print(f"{region} → The REGION DOES NOT EXIST. Consult the directory for existing regions: Data/Names/People")
        print(f"Error: {e}")
    finally:
        pass
    
    arr = open_txt(routh,size,repeat)
    return arr

def gen_female_name(region="latam",size=1,repeat=REPEAT):
    
    """ Generate a female name from a specific region and return an array of type np.array.
        You can add your own data in the Data/names/people directory. The suffix **female_** is required for the file names.
    
        + _Parameters_:
        1. region → choose names based on region (latam,north_america,asia)
        2. size → size of array
        3. repeat → unique valors o not (change whit false or true)
        
    """    
    region.lower()
    
    #Try catch to correct the errors
    try:
        routh = os.path.join(__FILE_ROUTH, f"female_{region}.txt")
    except Exception as e:
        print(f"{region} → The REGION DOES NOT EXIST. Consult the directory for existing regions: Data/Names/People")
        print(f"Error: {e}")
    finally:
        pass
    
    arr = open_txt(routh,size,repeat)
    return arr

def gen_surnames_region(region="latam",size=1,repeat=REPEAT):
    
    """ Generate a surname  from a specific region and return an array of type np.array.
        You can add your own data in the Data/names/people directory. The suffix **surnames_** is required for the file names.
    
        + _Parameters_:
        1. region → choose names based on region (latam,north_america,asia)
        2. size → size of array
        3. repeat → unique valors o not (change whit false or true)
        
    """    
    region.lower()
    
    #Try catch to correct the errors
    try:
        routh = os.path.join(__FILE_ROUTH, f"surnames_{region}.txt")
    except Exception as e:
        print(f"{region} → The REGION DOES NOT EXIST. Consult the directory for existing regions: Data/Names/People")
        print(f"Error: {e}")
    finally:
        pass
    
    arr = open_txt(routh,size,repeat)
    return arr


def gen_names(size=1,repeat=REPEAT):
    
    """ Generate a names and return an array of type np.array.
    
        + _Parameters_:
        1. size → size of array
        2. repeat → unique valors o not (change whit false or true)
        3. repeat → unique valors o not (change whit false or true)
        
    """    
    routh = os.path.join(__FILE_ROUTH, "names.txt")
    
    arr = open_txt(routh,size,repeat)
    return arr

def gen_surnames(size=1,repeat=REPEAT):
    
    """ Generate a names and return an array of type np.array.
    
        + _Parameters_:
        1. region → choose names based on region (latam,north_america,asia)
        2. size → size of array
        3. repeat → unique valors o not (change whit false or true)
        
    """    
    routh = os.path.join(__FILE_ROUTH, "surnames.txt")
    
    arr = open_txt(routh,size,repeat)
    return arr

def gen_full_name(size=1,repeat=REPEAT):
    
    arr1 = gen_names(size=size,repeat=NO_REPEAT)
    arr2 = gen_surnames(size=size,repeat=NO_REPEAT)
    arr3 = gen_surnames(size=size,repeat=NO_REPEAT)

    full_name = chooser3(size,arr1,arr2,arr3)

    return full_name