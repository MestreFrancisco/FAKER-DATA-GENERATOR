from random import randint , choice , uniform
from utils.numbers import abbreviate_number

class Company:
    """
        Company Class:
        ----------
            This class represents a simulated company with attributes and behaviors designed to reflect 
            various real-world business characteristics such as company size, value, industry, employee 
            satisfaction, and resource allocation. It generates synthetic data suitable for modeling, 
            testing, or educational simulations.

        Attributes:
            -----------
            - id (int): Unique identifier for the company.
            - name (str): Name of the company.
            - industry (str): The sector or industry in which the company operates.
            - size_category (str): Classification of the company by size. Accepted values:
            'micro', 'small', 'medium', 'large', 'extra', 'global'.
            - employee_count (int): Number of employees based on the size category.
            - company_value (str): Formatted representation of the company's total value.
            - company_value_no_abbreviate (float): Raw numerical value of the company.
            - country (str): Name of the randomly assigned country where the company operates.
            - phone_number (str): Simulated contact number based on the country’s calling code.
            - contact_email (str): Simulated email contact address for the company.
            - open_projects (float): Estimated number of ongoing projects.
            - min_work_hour (int): Minimum daily work hours in the company.
            - glassdoor_clasification (float): Simulated rating score (1.0 to 5.0) representing employee reviews.
            - best_place_to_work (bool): Flag indicating if the company has received a "Best Place to Work" recognition.
            - company_anual_budget (float): Estimated annual operating budget.
            - company_month_budget (float): Estimated monthly operating budget.
            - salary_anual_budget_percentage (str): Percentage of the budget allocated to salaries (as a string).
            - salary_anual_budget (float): Monetary amount allocated to salaries annually.
            - remote_friendly (bool): Whether the company supports remote work.
            - hiring (bool): Whether the company is currently hiring.
            - employee_satisfaction (str): Final calculated employee satisfaction percentage.

        Methods:
        --------
            - __init__(self, name, industry, size_category, id):
                Initializes a company instance with randomized but logically consistent attributes.

            - print_info(self):
                Prints a structured summary of the company’s details.

        Private Methods:
        ----------------
            - __employees_size(self, size_category):
                Returns a list with employee count and company value based on the size category.

        Notes:
        ------
            - This class requires a Country class (imported from `Classes.country_class`) with at least 
            `name` and `phone_cod` attributes.
            - Some utility functions such as `abbreviate_number` and `choice`, `randint`, `uniform` 
            (from the `random` module) must be available in the environment.
    """

   
    __slots__ = (
    "best_place_to_work", "company_anual_budget", "company_month_budget", "company_value",
    "company_value_no_abbreviate", "contact_email", "continent", "country", "employee_count",
    "employee_satisfaction", "glassdoor_clasification", "hiring", "id", "industry", "min_work_hour",
    "name", "open_projects", "phone_number", "province", "remote_friendly", "rest_days",
    "salary_anual_budget", "salary_anual_budget_percentage", "size_category", "total_work_hours",
    "url_best_place_to_work", "work_days")

    
    def __init__(self,name,industry,size_category,id):
        
         
        #Basic Data
        self.id = id;
        self.name = name;
        self.industry = industry;
        self.size_category = size_category;
       
        lista = self.employees_size(self.size_category);
        
        self.employee_count = lista[0];
        self.company_value  = abbreviate_number(lista[1],"");
        self.company_value_no_abbreviate = lista[1]
        
        self.contact_email = self.name.lower().replace(" ","")+"@falsegmail.com"
       
    #Presupuesto 
    def fill_budget_Data(self):
        #💱Resources
        self.company_anual_budget = (self.company_value_no_abbreviate * randint(15,50)) / 100
        self.company_month_budget = self.company_anual_budget / randint(9,14)
        porcentaje = randint(12,45) 
        self.salary_anual_budget_percentage = str(porcentaje)+"%" 
        self.salary_anual_budget = porcentaje*self.company_value_no_abbreviate / 100
    
    # RRHH
    def fill_rrhh_data(self):
        self.remote_friendly = choice([True, False]);
        self.hiring = choice([True, False]);    
        

    #Awards
    def fill_prices_data(self):
        self.glassdoor_clasification = round(uniform(1.0, 5.5), 2) 
        self.best_place_to_work = choice([True, False])
        
        if self.best_place_to_work==True:
            self.url_best_place_to_work="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQW2S4gNNATLYxRJZI6CBIYnf0_Lb8TycUPOQ&s"
        else:
            self.url_best_place_to_work=None
    
     #Employees Data       
    def fill_employee_data(self):
        
        self.open_projects = round(self.employee_count * uniform(1.0,5.0),0) 
        self.min_work_hour = randint(3,13);    
        
        if self.min_work_hour >= 10:
            self.work_days=randint(3,9);
            self.rest_days=randint(3,14);
        else:
            self.rest_days = randint(1,5);
            self.work_days = randint(4,14);
        
        self.total_work_hours = self.work_days*self.min_work_hour 
        
        
    #Datos Geograficos
    def fill_geographic_data(self):    
        #-list of countries
        selecciona = ["AFG","ARG","DEU","BRA","CHL",
                      "COL","USA","LVA","MEX","MNG",
                      "PNG","PYF","PRT","REU",
                      "ESH","SUR","SJM","UGA","VUT","MKD",
                      "MAC","LUX","PRY","VEN","CAN"];
        
        from Classes.country_class import Country
        
        countryobj = Country(choice(selecciona))
        
        self.country = countryobj.name
        self.province = countryobj.provinces[0]
        self.phone_number = countryobj.phone_cod.replace("'","")+" "+ str(randint(0,999))+"-"+str(randint(100,999)) + "-" + str(randint(1000,9999))
        self.continent =countryobj.continet
    
    #Filling Values:
    def fill_all_values(self,nofill=0):
        
        #💰 Resources
         self.fill_budget_Data();
        #👣 RRHH
         self.fill_rrhh_data();
        #🤓 employes
         self.fill_employee_data();
        #🌍 world
         if nofill == "country":
            pass
         else:
            self.fill_geographic_data();
            
        #🏆 prices
         self.fill_prices_data();
        #😝 sastifaction
         self.get_employee_satisfaction();
        
    def to_dict(self):
        return {slot: getattr(self, slot) for slot in self.__slots__}
    
    @staticmethod
    def employees_size(size_category):
        size_category = size_category.lower()
        
        config = {
            "micro":  {"employees_range": (1, 14), "value_range": (50_000, 500_000)},
            "small":  {"employees_range": (10, 75), "value_range": (300_000, 1_000_000)},
            "medium": {"employees_range": (51, 280), "value_range": (50_0000, 2_500_000)},
            "large":  {"employees_range": (250, 1200), "value_range": (1_900_000, 5_000_000)},
            "extra":  {"employees_range": (1001, 15000), "value_range": (3_900_000, 10_000_000)},
            "global": {"employees_range": (10001, 500000), "value_range": (9_000_000, 100_000_000)},}
        
        if size_category not in config:
            raise ValueError("Invalid size category. Valid categories: micro, small, medium, large, extra, global.")
        
        employees_min, employees_max = config[size_category]["employees_range"]
        value_min, value_max = config[size_category]["value_range"]
        
        employees = randint(employees_min, employees_max)
        company_value = employees / randint(5, 10) * randint(value_min, value_max)
        
        return employees, company_value
    
    #IF ABOUT EMPLOYEE SASTIFACTION         
    def get_employee_satisfaction(self):
        """ This feature provides employee satisfaction. It is important and mandatory to complete HR, 
        employee, and rewards data for proper use. Beacause the employee sastifaction use it data."""
        
        sastifaction = 0
        glassdoorpoint = self.glassdoor_clasification;
        hourpoints= self.min_work_hour;
        restdayspoints = self.rest_days;
        workdayspoint = self.work_days;
        
        #-----------------GlassdoorPoints
        if glassdoorpoint >= 5.0: sastifaction += 20
        elif glassdoorpoint >= 4.0: sastifaction += 10
        elif glassdoorpoint >= 3.0: sastifaction += 5
        elif glassdoorpoint >= 2.0: pass
        elif glassdoorpoint >= 1.5: sastifaction -= 5
        else: sastifaction -= 10

        #-----------------HoursPoints
        if hourpoints == 13: sastifaction -= 35
        elif hourpoints >= 10: sastifaction -= 5
        elif hourpoints >= 7: pass
        elif hourpoints >= 4: sastifaction += 5
        else: sastifaction += 35

        #-----------------RestDaysPoints
        if restdayspoints >= 12: sastifaction += 35
        elif restdayspoints >= 9: sastifaction += 15
        elif restdayspoints >= 6: sastifaction += 5
        elif restdayspoints >= 3: pass
        else: sastifaction -= 15

        #-----------------WorkDaysPoints
        if workdayspoint >= 12: sastifaction -= 35;
        elif workdayspoint >= 9: sastifaction -= 15;
        elif workdayspoint >= 6: pass
        elif workdayspoint >= 4: sastifaction += 5;
        else: sastifaction += 15;

        #----------------Adiotionals
        if self.remote_friendly == True:sastifaction+=3;
        
        randomExtraPoints =randint(10 , 20)    
        self.employee_satisfaction = str(sastifaction+randomExtraPoints)+"%"
        
    def update_data(self):
        #0 = not changes
        #1 = basic data
        #2 = budget changes
        #3 = employe data
        #4 = all Data 
        not_changes = choice([1,1,2,2,3,4])
        if(not_changes==4):
            #Basic Data
            lista = self.employees_size(self.size_category);
            self.employee_count = lista[0];
            self.company_value  = abbreviate_number(lista[1],"");
            self.company_value_no_abbreviate = lista[1]
            self.fill_all_values(nofill="country");
        
        elif (not_changes==3) : self.fill_employee_data();
        elif (not_changes==2) : self.fill_budget_Data();
        
        elif (not_changes==1):
            #Basic Data
            lista = self.employees_size(self.size_category);
            self.employee_count = lista[0];
            self.company_value  = abbreviate_number(lista[1],"");
            self.company_value_no_abbreviate = lista[1]
            
        