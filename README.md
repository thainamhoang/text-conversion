# Text Conversion
Created in needs of converting texts in pdf files to .txt file. Materials belong to [Professor Daniel Youd, Beloit College](https://www.beloit.edu/live/profiles/285-daniel-youd). 

## Instruction 

#### Windows 
Install Anaconda 

#### MacOS
Install Python latest version and brew. [Configure](https://opensource.com/article/19/5/python-3-default-mac) virtual environment.

#### On both machines
```
pip install pytesseract pillow pdf2image
```

#### Running

##### Python files
Run [pdf_to_image.py](/pdf_to_image.py) to convert pdf to images. Then using those images to convert to text by [image_to_text.py](/image_to_text.py)

##### Jupyter Notebooks
Run [pdf_to_image.ipynb](/pdf_to_image.ipynb) to convert pdf to images. Then using those images to convert to text by [image_to_text.ipynb](/image_to_text.ipynb)