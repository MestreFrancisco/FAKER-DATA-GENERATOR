from Classes.color import Color
from utils.data_loader import REPEAT
from numpy import random as nrd
from numpy import array as nparr
from numpy import uint8

COLOR_MAX = 832

def gen_colors(size=1, repeat=REPEAT, gamma="all", language="En"):
    """
    Generate a list of color names based on the specified language and color range.

    Parameters:
        size (int): Number of color names to generate.
        repeat (bool): Whether colors can be repeated in the output.
        gamma (str): A category or range of colors to filter by (e.g. "red","yellow", "all").
        language (str): Language code for color names. Only "En" (English) and "Es" (Spanish) are supported.

    Returns:
        np.ndarray: An array of randomly selected color names.

    Raises:
        ValueError: 
            - If repeat is False and the requested size exceeds the number of available colors.
            - If the specified language is not "En" or "Es".
    """
    #Rises
    if language not in {"En", "Es"}:
        raise ValueError(f"Invalid language '{language}'. Only 'En' and 'Es' are supported.")

    color_df = Color(size, repeat, gamma)
    np_array = color_df.color_df.select(language).to_numpy().flatten()

    #Rises
    if not repeat and size > len(np_array):
        raise ValueError(
            f"\n-Cannot generate {size} unique colors without repetition" 
            f"\n-the dataset has {len(np_array)} unique values."
            f"\n-Set `repeat=True` if you want to allow duplicates."
        )

    resultado = nrd.choice(np_array, size=size, replace=repeat)
    return resultado



def gen_random_hexcolor(size=1, repeat=REPEAT):
    """
    Generate an array of random hexadecimal color codes.

    Parameters:
        size (int): Number of hex color codes to generate.
        repeat (bool): Whether colors can repeat.

    Returns:
        np.ndarray: Array of hex color strings (e.g., '#A1B2C3').

    Raises:
        ValueError: If repeat is False and size exceeds the number of unique RGB combinations.
    """
    total_colors = 256 ** 3

    if not repeat and size > total_colors:
        raise ValueError(
            f"Cannot generate {size} unique hex colors. "
            f"The maximum possible is {total_colors}. Set `repeat=True` to allow duplicates."
        )

    if repeat:
        colors = [
            '#{0:02X}{1:02X}{2:02X}'.format(
                nrd.randint(0, 256),
                nrd.randint(0, 256),
                nrd.randint(0, 256)
            )
            for _ in range(size)
        ]
    else:
        # Sin repetición: generamos todos posibles y elegimos aleatoriamente
        all_possible = nparr([
            '#{0:02X}{1:02X}{2:02X}'.format(r, g, b)
            for r in range(256)
            for g in range(256)
            for b in range(256)
        ])
        colors = nrd.choice(all_possible, size=size, replace=False)

    return nparr(colors)


def gen_rgb(size=1, repeat=REPEAT):
    """
    Generate an array of random RGB color values.

    Parameters:
        size (int): Number of RGB colors to generate.
        repeat (bool): Whether colors can repeat.

    Returns:
        np.ndarray: Array of shape (size, 3) with RGB integer values in range 0-255.

    Raises:
        ValueError: If repeat is False and size exceeds the number of unique RGB combinations.
    """
    total_colors = 256 ** 3

    if not repeat and size > total_colors:
        raise ValueError(
            f"Cannot generate {size} unique RGB colors. "
            f"The maximum possible is {total_colors}. Set `repeat=True` to allow duplicates."
        )

    if repeat:
        return nrd.randint(0, 256, size=(size, 3), dtype=uint8)
    else:
        # Generamos todos posibles y elegimos sin reemplazo
        all_possible = nparr([
            (r, g, b)
            for r in range(256)
            for g in range(256)
            for b in range(256)
        ], dtype= uint8 )
        indices = nrd.choice(len(all_possible), size=size, replace=False)
        return all_possible[indices]


def gen_hex_matrix(rows, cols, repeat=REPEAT):
    """
    Generate a 2D matrix of random hexadecimal color codes.

    Parameters:
        rows (int): Number of rows in the matrix.
        cols (int): Number of columns in the matrix.
        repeat (bool): Whether colors can repeat in the matrix. Default is True.

    Returns:
        np.ndarray: A 2D numpy array of shape (rows, cols) with hex color strings.
    
    Raises:
        ValueError: If repeat is False and the total number of requested colors
                    exceeds the number of unique possible colors.
    """   
    total = rows * cols
    colors = gen_random_hexcolor(size=total, repeat=repeat)
    return colors.reshape((rows, cols))
    

def gen_hex_specific_color(size=1,hex="#000000"):
    return nparr([hex] * size)

def gen_black(size=1):
    """Generate an array of classic black color hex codes."""
    return nparr(["#000000"] * size)

def gen_white(size=1):
    """Generate an array of classic white color hex codes."""
    return nparr(["#FFFFFF"] * size)

def gen_red_basic(size=1):
    """Generate an array of classic red color hex codes."""
    return nparr(["#FF0000"] * size)

def gen_blue_basic(size=1):
    """Generate an array of classic blue color hex codes."""
    return nparr(["#0000FF"] * size)

def gen_green_basic(size=1):
    """Generate an array of classic green color hex codes."""
    return nparr(["#00FF00"] * size)

def gen_yellow_basic(size=1):
    """Generate an array of classic yellow color hex codes."""
    return nparr(["#FFFF00"] * size)

#------ better colors

def gen_red(size=1):
    """Generate an array of classic red color hex codes."""
    return nparr(["#AF2323"] * size)

def gen_blue(size=1):
    """Generate an array of classic blue color hex codes."""
    return nparr(["#2271B3"] * size)

def gen_green(size=1):
    """Generate an array of classic green color hex codes."""
    return nparr(["#009D71"] * size)

def gen_yellow(size=1):
    """Generate an array of classic yellow color hex codes."""
    return nparr(["#E9BD15"] * size)