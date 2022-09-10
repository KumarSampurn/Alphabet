import speech_recognition as sr
def stt():
 r = sr.Recognizer()
 with sr.Microphone() as source:     #install pyaudio module for microphone access
    r.adjust_for_ambient_noise(source)
    print("Say something:")
    audio=r.listen(source)
    try:
        text= r.recognize_google(audio)
        #print("You said : {}".format(text))
        print("You said : "+text)
    except: 
        print("Couldn't recognize properly")
stt()
