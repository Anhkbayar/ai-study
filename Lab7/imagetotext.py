import cv2
import pytesseract
from PIL import Image
import os

pytesseract.pytesseract.tesseract_cmd = r'G:\Tesseract\tesseract.exe'

img = cv2.imread('pic1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thres = cv2.threshold(gray, 141, 255, cv2.THRESH_BINARY)

custom_config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.,:-'

cv2.imwrite("debug_preprocessed.png", thres)

text = pytesseract.image_to_string(thres, lang='eng', config=custom_config)
print("Taniulsan text")
print(text)

with open('text1.txt','r',encoding='latin-1') as file:
    ground_truth = file.read()
    
def calculate_accuracy(pred, true):
    import difflib
    return difflib.SequenceMatcher(None, pred.strip(), true.strip()).ratio()

accuracy = calculate_accuracy(text, ground_truth)
print(f'Text taniltiin nariivchlal: {accuracy*100:.2f}%')
