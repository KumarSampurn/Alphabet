import cv2 

from skimage.metrics import structural_similarity
import imutils
import cv2

image_one=cv2.imread("C:/Users/tanb0/OneDrive/Documents/KODIKON/photos/pizza.jpg")
image_two=cv2.imread("C:/Users/tanb0/OneDrive/Documents/KODIKON/photos/pizzadup.jpg")

gray1=cv2.cvtColor(image_one,cv2.COLOR_BGR2GRAY )
gray2=cv2.cvtColor(image_two,cv2.COLOR_BGR2GRAY )

(score,diff)=structural_similarity(gray1,gray2,full=True)
diff=(diff * 255).astype("uint8")
print("SSIM: ()".format(score))

thresh=cv2.threshold(diff,0,128,cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU)[1]
cnts=cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts=imutils.grab_contours(cnts)

no_of_differences=0
for c in cnts:
    (x,y,w,h)=cv2.boundingRect(c)
    rect_area=w*h
    if rect_area>10:
        no_of_differences +=1
        # cv2.rectangle(image_one,(x,y),(x+w,y+h),(0,255,255),2)
        # cv2.rectangle(image_two,(x,y),(x+w,y+h),(0,255,255),2)
print("no differences=",no_of_differences)
cv2.imshow("original",image_one)
cv2.imshow("spot the difference",image_two)

cv2.waitKey(0)

