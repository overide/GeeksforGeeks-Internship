'''
Configure this file as you please
for tuning various settings parameters 
'''


# Path of template image
IMG_PATH = "assets/certificate.jpg"

# Path of excel sheet
XLS_PATH = "assets/names_xls.xlsx"

# Path of desired font file (.ttf)
FONT_PATH = "assets/Cylburn.ttf"

# Path where generated images get saved
TARGET_PATH = "certificates/"

# Size of font to use
FONT_SIZE = 45

# Color of font to use
FONT_COLOR = "black"

# Text which will be written on image
TXT_TEMPLATE = """We are happy to certify that Mr. {} 
has been chosen Geek of the Month for his excellent
contributions."""

# Column to extract (0 indexed)
TARGET_COL = 0

# Space between lines in pixels, default is 15
SPACING_PX = 15

# X coordinate for text
X = 240

# Y coordinate for text
Y = 270