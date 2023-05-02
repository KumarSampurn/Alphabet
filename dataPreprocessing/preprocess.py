##################PARAMETERS##################

DIMENSION= (640, 480)


DATABASE_PATH = 'db/m'
EXPORT_PATH = 'db/m_preprocessed'
LOWER_BOUND = [36, 24, 207]
UPPER_BOUND = [45, 60, 234]

##############################################


import cv2
import os
import numpy as np

def getImages(path):
    images=os.listdir(path)
    return images

def preprocess(img):
    img= cv2.resize(img,DIMENSION)
    kernel_size = (3, 3)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernel_size)
    img = cv2.erode(img, kernel, iterations = 1)
    img = cv2.dilate(img, kernel, iterations = 1)
    
    mask = cv2.inRange(img, np.array(LOWER_BOUND),np.array(UPPER_BOUND))
     
    # while True:
    #     cv2.imshow("img", img)
    #     cv2.imshow("mask", mask)
    #     if cv2.waitKey(1) & 0xFF == ord('q'):
    #         break
        
    return mask
  
        
images=getImages(DATABASE_PATH)

os.mkdir(EXPORT_PATH)
for i in range(len(images)):
    img=cv2.imread(DATABASE_PATH+'/'+images[i])
    mask=preprocess(img)
    
    cv2.imwrite(EXPORT_PATH+'/'+images[i],mask)

