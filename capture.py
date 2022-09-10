import cv2

cap=cv2.VideoCapture(0)

output= cv2.VideoWriter("output.avi", cv2.VideoWriter_fourcc(*'MPEG'),30,(1080,1920))

while True:
    try:
        ret, frame= cap.read()
        if(ret):
            # rectange
            cv2.rectangle(frame, (225,125),(425,325),(0.255,0))
            #verticle line
            cv2.rectangle(frame, (325, 175),(325,275),(0,255,0))
            #horizontal line
            cv2.rectangle(frame, (275, 225), (375, 225),(0, 255, 0))    

            output.write(frame)
            cv2.imshow("output",frame)
            key = cv2.waitKey(1)
        if key== ord('s'):
            cv2.imwrite(filename='captured_image_color.jpg', img=frame)
            cap.release()
            img_new = cv2.imread('captured_image_color.jpg', cv2.IMREAD_GRAYSCALE)
            img_new = cv2.imshow("Captured Image", img_new)
            cv2.waitKey(1650)
            cv2.destroyAllWindows()

            img_ = cv2.imread('captured_image_color.jpg', cv2.IMREAD_ANYCOLOR)

            gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)

            img_ = img_[125:325 , 225:425]

            img_resized = cv2.imwrite(filename='captured_image_greyscale-final.jpg', img=img_)
            print("Image saved!")

            break
        elif key == ord('q'):
            print("Turning off camera.")
            cap.release()
            print("Camera off.")
            print("Program ended.")
            cv2.destroyAllWindows()
            break

    except(KeyboardInterrupt):
        print("Turning off camera.")
        cap.release()
        print("Camera off.")
        print("Program ended.")
        cv2.destroyAllWindows()
        break
