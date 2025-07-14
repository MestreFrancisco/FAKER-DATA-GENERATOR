from Gen import names as gname
from Gen import country as gcountry
import random

class Persona:
    """
    he Persona class works as a wrapper around the name generator in names.py.  
    This class adds additional attributes such as name, age, contact email, country, and other basic data.  
    It is used to complete and add people to a dataset or to create an ID.  

    It continues using the generator from names.py to generate random names,  
    but adds this extra data to make the generated dataset more complex and diverse.

    of course you cand modify and add more data , o extends this class to make this Human and People data more complex.
     
    # Attributes:
    ---
    
    - name(str) → use gen_full_name() and his parameters
    - age(parameter is str but the value is int) → gen a random age whit parameters , here the list.
    
    > - all → 1-100.
    > - adults → 18-50.
    > - young_adults → 18-30.
    > - old → 60-99.
    > - kids → 4-13.
    
    - country(str) → geograpich data.
    - mailcontact (str) → mail contact.
    """
    __slots__=("id","name","country","age","mailcontact")
   
    def __init__(self,id,age="adults"):
        
        self.id = int(id)+1
        self.name =  gname.gen_full_name()[0]
        
        if age=="all":self.age = random.randint(1, 100);
        elif age=="adults":self.age =  random.randint(18, 50);
        elif age=="kids":self.age =  random.randint(4, 13);
        elif age=="youngs_adults":self.age =  random.randint(18, 30);
        elif age=="old":self.age =  random.randint(60, 99);
        
        self.country = gcountry.gen_countrys()[0]
        self.mailcontact = self.name.replace(" ","").lower()+str(random.randint(0, 999))+"@gmail.com"
    
    
    def to_dict(self):
        return {slot: getattr(self, slot) for slot in self.__slots__}
    
    