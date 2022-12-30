import cv2 as cv
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
from skimage import io
from skimage.transform import rotate
from skimage.color import rgb2gray
from deskew import determine_skew

def binarisation(img):
    img = cv.imread(img,0)
    img = cv.medianBlur(img,5)
    ret,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
    th2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,\
                cv.THRESH_BINARY,11,2)
    th3 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
                cv.THRESH_BINARY,11,2)
    titles = ['Original Image', 'Global Thresholding (v = 127)',
                'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
    images = [img, th1, th2, th3]
    return th3
  #for i in range(3,4):
      #plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
      #plt.title(titles[i])
      #plt.xticks([]),plt.yticks([])
  #plt.show()

def noise(img):
    dst = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)
    return dst
  #plt.subplot(121),plt.imshow(img)
  #plt.subplot(122),plt.imshow(dst)
  #plt.show()

def deskew(_img):
    image = io.imread(_img)
    grayscale = rgb2gray(image)
    angle = determine_skew(grayscale)
    rotated = rotate(image, angle, resize=True) * 255
    return rotated.astype(np.uint8)

def display_avant_apres(_original):
    plt.subplot(1, 2, 1)
    plt.imshow(io.imread(_original))
    plt.subplot(1, 2, 2)
    plt.imshow(deskew(_original))

def preprocessing(img):
    img=binarisation(img)
    img=noise(img)
    img=deskew(img)
