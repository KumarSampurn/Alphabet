from skimage.metrics import structural_similarity
import imutils
import cv2


def capture_image():
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

                gray = gray[125:325 , 225:425]

                

                img_resized = cv2.imwrite(filename='captured_image_greyscale-final.jpg', img=gray)
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


def compare_image(image_one , image_two):
    
    gray1=cv2.cvtColor(image_one,cv2.COLOR_BGR2GRAY )
    gray2=cv2.cvtColor(image_two,cv2.COLOR_BGR2GRAY )

    gray1= cv2.blur(gray1,(6,6))
    gray2= cv2.blur(gray2,(6,6))


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
            cv2.rectangle(image_one,(x,y),(x+w,y+h),(0,255,255),2)
            cv2.rectangle(image_two,(x,y),(x+w,y+h),(0,255,255),2)
    print("no differences=",no_of_differences)
    cv2.imshow("original",image_one)
    cv2.imshow("spot the difference",image_two)

    cv2.waitKey(0)






def letter_A():
    
    test_img=cv2.imread(r"C:\Users\KUMAR SAMPURN\Documents\Kodikon\database\A.jpeg")
    capture_image()
    captured_image=cv2.imread("captured_image_greyscale-final.jpg")
    captured_image=cv2.imread(r"C:\Users\KUMAR SAMPURN\Documents\Kodikon\database\bad_A.jpeg")
    
    
    width = 500
    height = 500
    dim = (width, height)

    test_img = cv2.resize(test_img, dim, interpolation = cv2.INTER_AREA)
    test_img= test_img[10:-10  , 20:-20]

    
    captured_image = cv2.resize(captured_image, dim, interpolation = cv2.INTER_AREA)
    captured_image= captured_image[10:-10  , 20:-20]
    compare_image(test_img, captured_image)

def letter_B():
    
    test_img=cv2.imread(r"C:\Users\KUMAR SAMPURN\Documents\Kodikon\database\B.jpeg")
    capture_image()
    captured_image=cv2.imread("captured_image_greyscale-final.jpg")
    #captured_image=cv2.imread(r"C:\Users\KUMAR SAMPURN\Documents\Kodikon\database\bad_A.jpeg")
    
    
    width = 500
    height = 500
    dim = (width, height)

    test_img = cv2.resize(test_img, dim, interpolation = cv2.INTER_AREA)
    test_img= test_img[10:-10  , 20:-20]

    
    captured_image = cv2.resize(captured_image, dim, interpolation = cv2.INTER_AREA)
    captured_image= captured_image[10:-10  , 20:-20]
    compare_image(test_img, captured_image)





def main():
    print("\t\t\t\t\t\tHello!! How are you doing?")
    print("\t\t\t\t\t  What do you want to do today?")
    print("\t\t\t\t\t\tModule 1 : Alphabet 'A'")
    print("\t\t\t\t\t\tModule 2 : Alphabet 'B'")

    print("Enter Choice : ")
    ch=(input())
    
    if ch=='1':
        letter_A()
    if ch=='1':
        letter_A()


if __name__ == '__main__':
    main()
