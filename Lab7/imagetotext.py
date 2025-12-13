import cv2
import pytesseract
from PIL import Image
import os

img = cv2.imread('pic1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thres = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

text = pytesseract.image_to_string(thres, lang='eng')
print("Taniulsan text")
print(text)

with open('text1.txt','r',encoding='latin-1') as file:
    ground_truth = file.read()
    
def calculate_accuracy(pred, true):
    import difflib
    return difflib.SequenceMatcher(None, pred.strip(), true.strip()).ratio()

accuracy = calculate_accuracy(text, ground_truth)
print(f'Text taniltiin nariivchlal: {accuracy*100:.2f}%')
