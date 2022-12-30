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


def detect_text_blocks(img_path):
    detection_result = reader.detect(img_path,
                                 width_ths=0.7, 
                                 mag_ratio=1.5
                                 )
    text_coordinates = detection_result[0][0]
    return text_coordinates




def draw_bounds(img_path, bbox):
    image = Image.open(img_path)  
    draw = ImageDraw.Draw(image)
    for b in bbox:
        p0, p1, p2, p3 = [b[0], b[2]], [b[1], b[2]], \
                         [b[1], b[3]], [b[0], b[3]]
        draw.line([*p0, *p1, *p2, *p3, *p0], fill='red', width=2)
    return np.asarray(image)




def coordinates_to_df(text_coordinates,df,img_path):
    for coord in text_coordinates:
        x_min, y_min, x_max, y_max = coord[0], coord[2], \
                                    coord[1], coord[3]
        
        if x_min >= 0 and x_max >= 0 and \
        y_min >= 0 and y_max >= 0:
            im2 = cv2.imread(img_path)
            cropped = im2[y_min:y_max, x_min:x_max]
            text = ocr.ocr(cropped,
                        det=False,
                        cls=False
                        )
            df2 = {'coord': coord, 'text': text[0][0][0]}
            df = df.append(df2, ignore_index = True)
            print("{}: {}".format(coord, text[0][0][0]))


def final_plot(img_path,boxe):
    text_blocks_in_image = draw_bounds(img_path, boxe)
    plt.figure(figsize = (200,20))
    plt.imshow(text_blocks_in_image)

def find_file(img_path,train_data):
    lis = []
    return lis

def get_coord_df(labels,df):
    for i in labels:
        df_ans=df[df['text'].str.contains(i)]
        real=real.append(df_ans.iloc[0], ignore_index = True)


def add_to_table(File_name,df,table):
    df.loc[len(df)] = list
    table.loc[len(table)] = File_name
