from PIL import Image
import pytesseract as tr

text = tr.image_to_string(Image.open(r'D:\C\image.png'))
print(text)
