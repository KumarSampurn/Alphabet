import cv2
path=r'C:\Users\tanb0\OneDrive\Documents\KODIKON\photos\pizzadup.jpg'
src=cv2.imread(path)
image=cv2.flip(src,1)

window_name='Image'

cv2.imshow(window_name,image)
cv2.waitKey(0)
