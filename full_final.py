from skimage.metrics import structural_similarity
import imutils
import cv2
import time
import speech_recognition as sr
from gtts import gTTS
import os

print("Press 1. for Handwriting , 2. for Pronounciation ")
n1=int(input())
flag=0
if(n1==1):
    def capture_image():
        cap=cv2.VideoCapture(1)

        output= cv2.VideoWriter("output.avi", cv2.VideoWriter_fourcc(*'MPEG'),30,(1080,1920))

        while True:
            try:
                ret, frame= cap.read()
                if(ret):
                    # rectange
                    cv2.rectangle(frame, (195,175),(460,450),(0.255,0))
                    #verticle line
                    cv2.rectangle(frame, (328, 265),(328,360),(0,255,0))

                    #horizontal line1
                    
                    cv2.rectangle(frame, (285, 312), (370, 312),(0, 255, 0))    
                    frame=cv2.flip(frame,1)
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

                    gray=gray[165 : 460 , 1455:1730]
                    gray=gray[12:-12 , 12:-12]

                    

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

        gray1= cv2.blur(gray1,(5,5))
        gray2= cv2.blur(gray2,(5,5))


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
        #  cap= cv2.VideoCapture(r'C:\Users\pratj\OneDrive\Documents\Final\A.mp4')


        # fps= int(cap.get(cv2.CAP_PROP_FPS))

        # # print("This is the fps ", fps)

        # if cap.isOpened() == False:
        #     print("Error File Not Found")

        # while cap.isOpened():
        #     ret,frame= cap.read()

        #     if ret == True:

        #         time.sleep(1/fps)

        #         cv2.imshow('frame', frame)

        #         if cv2.waitKey(1) & 0xFF == ord('q'):
        #             break

        #     else:
        #         break


        # cap.release()
        # cv2.destroyAllWindows()


        

        # capture=cv2.VideoCapture(r'C:\Users\pratj\OneDrive\Documents\Final\A.mp4')
        # frame=capture.read()
        # while frame!=0:
        #     isTrue, frame=capture.read()
        
        #     cv2.imshow('Video',frame)
        #     if cv2.waitKey(20) & 0xFF==ord('d'):
        #         break
        # capture.release()
        # cv2.destroyAllWindows()
        test_img=cv2.imread(r"C:\Users\pratj\OneDrive\Documents\Final\database\A.jpeg")
        capture_image()
        captured_image=cv2.imread("captured_image_greyscale-final.jpg")
        # captured_image=cv2.imread(r"C:\Users\pratj\OneDrive\Documents\Final\database\bad_A.jpeg")
        
        
        width = 500
        height = 500
        dim = (width, height)

        test_img = cv2.resize(test_img, dim, interpolation = cv2.INTER_AREA)
        test_img= test_img[10:-10  , 20:-20]

        
        captured_image = cv2.resize(captured_image, dim, interpolation = cv2.INTER_AREA)
        captured_image= captured_image[10:-10  , 20:-20]
        compare_image(test_img, captured_image)

    def letter_B():
        
        cap= cv2.VideoCapture(r'C:\Users\pratj\OneDrive\Documents\Final\B.mp4')


        fps= int(cap.get(cv2.CAP_PROP_FPS))

        # print("This is the fps ", fps)

        if cap.isOpened() == False:
            print("Error File Not Found")

        while cap.isOpened():
            ret,frame= cap.read()

            if ret == True:

                time.sleep(1/fps)

                cv2.imshow('frame', frame)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            else:
                break


        cap.release()
        cv2.destroyAllWindows()
        test_img=cv2.imread(r"C:\Users\pratj\OneDrive\Documents\Final\database\B.jpeg")
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

    def letter_C():
        
        cap= cv2.VideoCapture(r'C:\Users\pratj\OneDrive\Documents\Final\C.mp4')


        fps= int(cap.get(cv2.CAP_PROP_FPS))

        print("This is the fps ", fps)

        if cap.isOpened() == False:
            print("Error File Not Found")

        while cap.isOpened():
            ret,frame= cap.read()

            if ret == True:

                time.sleep(1/fps)

                cv2.imshow('frame', frame)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            else:
                break


        cap.release()
        cv2.destroyAllWindows()
        test_img=cv2.imread(r"C:\Users\pratj\OneDrive\Documents\Final\database\C.jpeg")
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
        print("\t\t\t\t\t  For ")
        print("\t\t\t\t\t  What do you want to do today?")
        print("\t\t\t\t\t\tModule 1 : Alphabet 'A'")
        print("\t\t\t\t\t\tModule 2 : Alphabet 'B'")

        print("Enter Choice : ")
        ch=(input())
        
        if ch=='1':
            letter_A()
        if ch=='2':
            letter_B()


    if __name__ == '__main__':
        main()
elif(n1==2):
    print("Press 1. for letter A \n Press 2. for letter B \n Press 3. for letter C")
    n2=int(input())
    if(n2==1):

        r = sr.Recognizer()
        text=""
        with sr.Microphone() as source: 
            r.adjust_for_ambient_noise(source)
            print("Say A:")
            audio=r.listen(source)
            try:
                text= r.recognize_google(audio)
                text=text.upper()
                print("You said : "+text)
            except: 
                print("Couldn't recognize properly")
        # text=text.upper()
        if text == 'A':   
                    flag=1
                    mytxt = 'perfect!,move on to the next module'
                    language1 = 'en'
                    myobj1 = gTTS(text=mytxt, lang=language1, slow=False)
                    myobj1.save("output1.mp3")
                    os.system("start output1.mp3")
        first= text.index('A')
    elif(n2==2):
        r = sr.Recognizer()
        text=""
        with sr.Microphone() as source: 
            r.adjust_for_ambient_noise(source)
            print("Say B:")
            audio=r.listen(source)
            try:
                text= r.recognize_google(audio)
                text=text.upper()
                print("You said : "+text)
            except: 
                print("Couldn't recognize properly")
        # text=text.upper()
        if text == 'B':   
                    flag=1
                    mytxt = 'perfect!,move on to the next module'
                    language1 = 'en'
                    myobj1 = gTTS(text=mytxt, lang=language1, slow=False)
                    myobj1.save("output1.mp3")
                    os.system("start output1.mp3")
        first= text.index('B')
    elif(n2==3):
        r = sr.Recognizer()
        text=""
        with sr.Microphone() as source: 
            r.adjust_for_ambient_noise(source)
            print("Say C:")
            audio=r.listen(source)
            try:
                text= r.recognize_google(audio)
                text=text.upper()
                print("You said : "+text)
            except: 
                print("Couldn't recognize properly")
        # text=text.upper()
        if text == 'C':  
                    flag=1 
                    mytxt = 'perfect!,move on to the next module'
                    language1 = 'en'
                    myobj1 = gTTS(text=mytxt, lang=language1, slow=False)
                    myobj1.save("output1.mp3")
                    os.system("start output1.mp3")
        first= text.index('C')
    if (flag!=1):

        if first == 0:
            mytext = text[1:]
        elif (first>0) :
            mytext = 'Oh no! ,you said' + text[0:first] +'at the begining  and' + text[(first+1):] +'at the end'
        else :
            mytext = 'wrong word'
        language = 'en'

        myobj = gTTS(text=mytext, lang=language, slow=False)

        myobj.save("output.mp3")

        os.system("start output.mp3")
