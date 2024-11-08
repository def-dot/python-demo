import pytesseract
from PIL import Image

img = Image.open("1.jpg")
text = pytesseract.image_to_string(img, lang="chi_sim")
print(text)
