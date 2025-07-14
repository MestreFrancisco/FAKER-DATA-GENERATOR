from utils.data_loader import open_csv,open_parquet,REPEAT

class Color:
    
    """
    EN
    ---
    The Color class contains a complete dataset of colors that you can use to manipulate the table.

    Attributes:
        The attributes are synchronized, so if you want to get the hex color of 
        `colornames[0]`, you only need to access `color_hex[0]`.

        - `.color_df` (DataFrame): A DataFrame containing all the colors. Use .head() to limit the output.
        - `.colornames` (list of str): List of color names in English.
        - `.colornames_es` (list of str): List of color names in Spanish.
        - `.color_hex` (list of str): List of hexadecimal color codes.
        - `.image_url` (url str): List of url image to visualize the color
        - `.rgb` (list of int): List of all RGB color values.
        
    """
    
    colornames = [];
    colornames_es = [];
    color_hex = [];
    image_url = [];
    rgb = [];
    
    #-------------------CONSTRUCTOR
    def __init__(self, size=1 ,repeat=REPEAT , color_range="all"):
        self.color_df = self.__gen_colors(size,repeat,color_range)# ← Size repeat Color Range 
        self.__fillAtributes()
        
    def __gen_colors(self,size=1,repeat=REPEAT,color_range="all"): # ← Size y Color Range
        """ Generate a DataFrame of colors"""
        if color_range=="all":
            color_range="colors"
            df = open_parquet(f"Data/colors/"+color_range+".parquet")
            return df
        else:
            pass
        try: # ← verify if csv exist 
            df = open_csv(f"Data/colors/"+ color_range.lower()+ ".csv")
            return df
        except: # ← return error 
            raise("not exist , verify this in Data/colors")
            return 0
    
    def __fillAtributes(self):
        self.colornames = self.color_df.select(["En"])["En"].to_list()  
        self.colornames_es = self.color_df.select(["Es"])["Es"].to_list()
        self.color_hex = self.color_df.select(["hex_cod"])["hex_cod"].to_list()
        self.rgb = self.color_df.select(["RGB"])["RGB"].to_list()
        self.image_url = self.color_df.select(["image_url"])["image_url"].to_list()


        "image_url,Es,En,en_2,hex_cod,RGB"
    