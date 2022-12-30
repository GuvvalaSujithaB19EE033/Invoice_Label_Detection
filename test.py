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
from .template_matching import documentSimilarity

img_path=input()

preprocessing(img_path)

res_list=[]

for i in templates:
    d=documentSimilarity(i, img_path)
    res_list.append(d)
  
minpos = templates.index(min(templates))

data = pd.read_csv("table.csv")
lis=data.iloc[minpos].values.tolist()
draw_bounds(img_path, lis)

