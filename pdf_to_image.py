# Import dependencies
import pdf2image as p2i
import os

# Conversion
path_pdf = '/Users/thainam/Documents/GitHub/text-conversion/data/test_file.pdf' # File path
pages = p2i.convert_from_path(path_pdf, 350) # Convert from path, @param: dir, dpi value
path_pdf = path_pdf[:-4] # Tuple constant

# Save files
for page in pages:
    page.save("%s_%d.jpg" % (path_pdf, pages.index(page)), "JPEG") # Save and enumerate file names, extension "JPEG"