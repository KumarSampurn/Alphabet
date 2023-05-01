import cv2
import os

sampleImages = os.listdir("./assests")
sampleImages.sort()
# print(sampleImages)

goodImage= cv2.imread("./assests/"+sampleImages[len(sampleImages)-1])
badImages=[]
for pathname in sampleImages:
    badImages.append(cv2.imread("./assests/"+pathname))
    # print(badImages)

badImages.pop()


differenceImage= cv2.subtract(goodImage, badImages[0])


while True:
    cv2.imshow("Good Image", goodImage)
    
    cv2.imshow("Bad Image", badImages[0])
    cv2.imshow("Difference Image", differenceImage)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break