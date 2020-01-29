# Import dependencies
import pytesseract as pyt 
from PIL import Image

# Conversion
path_img = 'data/test_file_0.jpg' # File path
img = Image.open(path_img) # Open image
width, height = img.size # Define image size

# Parameter for image.crop: left, top, right, bottom
# Default: left = 0, top = 0, right = width, bottom = height

img_crop = img.crop((width / 3.14, 275, width, height * 5 / 6)) # Create a new object aka a cropped image
img_crop.show() # Show image

text = pyt.image_to_string(img_crop) # OCR images to text string

# Save file
file = open("file.txt", "a+") # Append texts into text file, text file will be create if not existed
file.write("\n") # New line
file.write(text) # Add texts

file.close() # Close