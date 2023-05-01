###################### Parameters #####################

SAMPLE_SIZE=500


NUMBER_OF_GOOD_IMAGES= (int)(0.7*SAMPLE_SIZE)
NUMBER_OF_BAD_IMAGES =(int)(0.3*SAMPLE_SIZE)

GOOD_IMAGES_PATH = "datasetCreation/dbCreationImages/goodImages"
BAD_IMAGES_PATH="datasetCreation/dbCreationImages/badImages" 

EXPORT_PATH="db"

LETTER = 'm'

FOLDER_NAME= EXPORT_PATH + '/' + LETTER

#######################################################

import os
import cv2
import shutil

if os.path.exists(FOLDER_NAME):
    shutil.rmtree(FOLDER_NAME)

os.mkdir(FOLDER_NAME)

goodImages=os.listdir(GOOD_IMAGES_PATH)
badImages=os.listdir(BAD_IMAGES_PATH)

# print(goodImages)
# print(badImages)

# print(len(goodImages))
# print(len(badImages))


oneGoodImageCount=NUMBER_OF_GOOD_IMAGES//(len(goodImages))
# print(oneGoodImageCount)
for i, goodImage in enumerate(goodImages):
    img = cv2.imread(GOOD_IMAGES_PATH+'/'+goodImage)
    for j in range(oneGoodImageCount):
        output_name = 'good_image_' + str(i) + '_' + str(j) + '.jpg'
        cv2.imwrite(FOLDER_NAME + '/' + output_name, img)
        
        
        
oneBadImageCount=NUMBER_OF_BAD_IMAGES//(len(badImages))
print(oneBadImageCount)
for i, badImage in enumerate(badImages):
    img = cv2.imread(BAD_IMAGES_PATH+'/'+badImage)
    for j in range(oneBadImageCount):
        output_name = 'bad_image_' + str(i) + '_' + str(j) + '.jpg'
        cv2.imwrite(FOLDER_NAME + '/' + output_name, img)
        
print("Done")
        
        
        






