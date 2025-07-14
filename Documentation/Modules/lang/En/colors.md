# 📒 MODULE `colors.py`

- Back to [Fake Data Generator README](../../../../README.md)
- Next module [📒 Module company](company.md)

The `Colors` module allows you to generate colors in different formats in an organized way.  
---
This module provides functions to generate colors in various formats and styles:

- Color names based on a Wikipedia dataset (833 named colors)  
- Random colors in hexadecimal format  
- Random colors in RGB format  
- 2D matrices of hexadecimal colors  
- Specific classic hexadecimal colors (black, white, red, blue, green, yellow)  

## Main Functions

### Name Generator Function
This function returns an array of random color names using a Wikipedia dataset with a total of 833 named colors.  
If you want to explore more attributes of the dataset, you can instantiate the `Color` object.

| Function           | Description                        |
|--------------------|------------------------------------|
| `gen_colors()`     | Generates an array of color names  |

#### 🟡 Unique Parameters
- `gamma="all"`  → Allows choosing the color range or gamma. See the full list in `Data/Colors`
- `language="En"` → Allows selecting the language. Only `"En"` and `"Es"` are supported. Any other value will raise an error.

### Color Code Generator Functions
These functions generate hexadecimal and RGB color codes.  
With these generators, you can create every possible color combination, or generate arrays of a single color to create images pixel by pixel — useful for:

- Creating unique or random color palettes  
- Generating pixel-by-pixel image data from color matrices  
- Visualizing data or building interactive charts/interfaces  
- Generating synthetic data for image processing or machine learning tests  
- Filling areas with solid or uniform colors  

| Function                   | Brief Description                                               |
|---------------------------|------------------------------------------------------------------|
| `gen_random_hexcolor`     | Generates a list of random hex colors.                          |
| `gen_rgb`                 | Generates a list of RGB format colors.                          |
| `gen_hex_matrix`          | Generates a 2D matrix of hex colors.                            |
| `gen_hex_specific_color`  | Generates an array with a single specified hex color.           |
| `gen_black`               | Generates an array of classic black (`#000000`).                |
| `gen_white`               | Generates an array of classic white (`#FFFFFF`).                |
| `gen_red_basic`           | Generates an array of classic red (`#FF0000`).                  |
| `gen_blue_basic`          | Generates an array of classic blue (`#0000FF`).                 |
| `gen_green_basic`         | Generates an array of classic green (`#00FF00`).                |
| `gen_yellow_basic`        | Generates an array of classic yellow (`#FFFF00`).               |
| `gen_red`                 | Generates a softer modern red (`#AF2323`).                      |
| `gen_blue`                | Generates a softer blue (`#2271B3`).                            |
| `gen_green`               | Generates a more modern green (`#009D71`).                      |
| `gen_yellow`              | Generates a warmer yellow (`#E9BD15`).                          |

---

## 💡 Usage Examples

```python
from Gen import color as gcolor 

# 1. Generate 10 random hex colors
colors = gcolor.gen_random_hexcolor(size=10)

# 2. Create a 5x5 matrix with unique colors
matrix = gcolor.gen_hex_matrix(5, 5, repeat=False)

# 3. Generate 100 RGB colors
rgb_array = gcolor.gen_rgb(size=100)

# 4. Fill an image with improved green color
green_pixels = gcolor.gen_green(size=10000)
