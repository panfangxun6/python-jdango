import pytesseract
from PIL import Image


def testImage():
    img = Image.open('test.png')
    text = pytesseract.image_to_string(img, lang='chi_sim')
    print(text)

testImage()