import pytesseract
from PIL import Image
from gtts import gTTS
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Tanveer\AppData\Local\Tesseract-OCR\tesseract.exe'
img = Image.open('text.png')
mytext = pytesseract.image_to_string(img)
language = 'en'
output = gTTS(text=mytext, lang=language, slow=False)
output.save('Image_speech.mp3')

os.system('start Image_speech.mp3')
