import pandas as pd
import numpy as np 
from paddleocr import PaddleOCR, draw_ocr
import cv2
import easyocr
import numpy as np
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt

reader = easyocr.Reader(['en'])
ocr = PaddleOCR(lang='en')

from .util import detect_text_blocks,draw_bounds,coordinates_to_df,final_plot,find_file,get_coord_df,add_to_table
from .preprocessing import preprocessing

img_path=input()

preprocessing(img_path)
text_coordinates = detect_text_blocks(img_path)
#print("The coordinates are: ",text_coordinates)

df = pd.DataFrame(columns=['coord','text'])

coordinates_to_df(text_coordinates,df,img_path)

draw_bounds(img_path, text_coordinates)

df['text'] = df['text'].astype(str)

labels = find_file(img_path,train_data)

real=pd.DataFrame(columns=['coord','text'])

get_coord_df(labels,df)

File_Name = [[img_path]]

for i in real['coord']:
  File_Name.append(i)

add_to_table(File_Name,df,table)
