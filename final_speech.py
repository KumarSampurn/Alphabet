import speech_recognition as sr
from gtts import gTTS
import os


r = sr.Recognizer()
text=""
with sr.Microphone() as source: 
    r.adjust_for_ambient_noise(source)
    print("Say something:")
    audio=r.listen(source)
    try:
        text= r.recognize_google(audio)
        print("You said : "+text)
    except: 
        print("Couldn't recognize properly")
text=text.upper()
first= text.index('A')

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
