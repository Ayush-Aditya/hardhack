"""
code for google colab
pip install easyocr
!pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib
from google.colab import drive
drive.mount('/content/drive')
!pip install Pillow
from PIL import Image
"""
import matplotlib.pyplot as plt
import cv2
import  easyocr
from pylab import rcParams
from IPython.display import Image
rcParams['figure.figsize']=8,16

def extract_text_from_image(image_path, reader):
    image = Image.open(image_path)
    results = reader.readtext(image_path)

    # Extracted text is stored in the 'text' field of the results
    text = ' '.join(result[1] for result in results)
    return text

# Specify the path to the image
image_path = '/content/5.png'

# Specify the language for OCR (e.g., 'en' for English)
language = 'en'

# Create an EasyOCR reader object
reader = easyocr.Reader([language])

# Extract text from the image
extracted_text = extract_text_from_image(image_path, reader)

# Specify the path to the text file
output_file_path = "/content/hello.txt"

# Open the file in write mode and write the extracted text
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write(extracted_text)

print(f"Extracted text saved to {output_file_path}")