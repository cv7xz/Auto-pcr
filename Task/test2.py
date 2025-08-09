import pytesseract
from PIL import Image

from utils import *
from window import BaseWindow
import csv

while True:
    print(ag.position())
    time.sleep(1)


# nameBox = (666,200,1200,240)

# with open(file = '1.csv',mode='a', encoding = 'utf-8',newline = '') as f:
#     writer = csv.writer(f)
#     Task = BaseWindow()
#     for i in range(115):
#         nameImage = Task.CaptureBox(nameBox)
#         name = GetText(nameImage)
#         name_box, name_text,conf = name[0]
#         print(name_text)
#         writer.writerow([name_text])
#         time.sleep(0.5)
#         click(rightPage)
