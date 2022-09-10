import cv2
import numpy as np

img=cv2.imread("0")
cv2.imshow("original image",img)
cv2.waitKey(0)

grey_img=cv2.cvtColor(img,cv2.COLOR_BRG2GRAY)
grey_img=cv2.bitwise_not(grey_img)

coordinates=np.column_stack(np.where(grey_img>0))
ang=cv2.minAreaRect(coordinates)[-1]

if ang<-45:
    ang=-(90+ang)
else:
    ang=-ang
print(ang)

height,width=img.shape[:2]
center_img=(width/2,height/2)

rotationMatrix=cv2.getRotationMatrix2D(center_img,ang,1.0)
rotated_img=cv2.warpAffine(img,rotationMatrix,(width+30,height),borderMode=cv2.BORDER_REFLECT)

cv2.imshow("rotated image",rotated_img)
cv2.waitKey(0)