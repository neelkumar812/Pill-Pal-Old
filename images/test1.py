import command as cmd
from tesseract import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'
img = cv2.imread('test_2.png') 
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow('result: ', img)
cv2.waitKey(0)
