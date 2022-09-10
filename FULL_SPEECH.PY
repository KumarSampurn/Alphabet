switch(c)
{
    case 1:
        from gtts import gTTS
        import os
        import speech_recognition
        UserVoiceRecognizer = speech_recognition.Recognizer()
        print("speak something:")
        while(1):
            try:

                with speech_recognition.Microphone() as UserVoiceInputSource:
        
                    UserVoiceRecognizer.adjust_for_ambient_noise(UserVoiceInputSource, duration=0.5)
        
                    # The Program listens to the user voice input.
                    UserVoiceInput = UserVoiceRecognizer.listen(UserVoiceInputSource)
        
                    UserVoiceInput_converted_to_Text = UserVoiceRecognizer.recognize_google(UserVoiceInput)
                    UserVoiceInput_converted_to_Text = UserVoiceInput_converted_to_Text.upper()
                    print(UserVoiceInput_converted_to_Text)
                    first=UserVoiceInput_converted_to_Text.index('A')
                    # last=UserVoiceInput_converted_to_Text.rindex()
                    if first == 0:
                        mytext = UserVoiceInput_converted_to_Text[1:]
                    elif (first>0) :
                        mytext = 'Oh no! ,you said' + UserVoiceInput_converted_to_Text[0:first] +'at the begining  and' + UserVoiceInput_converted_to_Text[(first+1):] +'at the end'
                    else :
                        mytext = 'wrong word'

                        # Language we want to use
                    language = 'en'

                    myobj = gTTS(text=mytext, lang=language, slow=False)

                    myobj.save("output.mp3")

        # Play the converted file
                    os.system("start output.mp3")
                        
            except KeyboardInterrupt:
                print('A KeyboardInterrupt encountered; Terminating the Program !!!')
                exit(0)

            except speech_recognition.UnknownValueError:
                print("No User Voice d+etected OR unintelligible noises detected OR the recognized audio cannot be matched to text !!!")
            break
        case 2:
            from gtts import gTTS
        import os
        import speech_recognition
        UserVoiceRecognizer = speech_recognition.Recognizer()
        print("speak something:")
        while(1):
            try:

                with speech_recognition.Microphone() as UserVoiceInputSource:
        
                    UserVoiceRecognizer.adjust_for_ambient_noise(UserVoiceInputSource, duration=0.5)
        
                    # The Program listens to the user voice input.
                    UserVoiceInput = UserVoiceRecognizer.listen(UserVoiceInputSource)
        
                    UserVoiceInput_converted_to_Text = UserVoiceRecognizer.recognize_google(UserVoiceInput)
                    UserVoiceInput_converted_to_Text = UserVoiceInput_converted_to_Text.upper()
                    print(UserVoiceInput_converted_to_Text)
                    first=UserVoiceInput_converted_to_Text.index('B')
                    # last=UserVoiceInput_converted_to_Text.rindex()
                    if first == 0:
                        mytext = UserVoiceInput_converted_to_Text[1:]
                    elif (first>0) :
                        mytext = 'Oh no! ,you said' + UserVoiceInput_converted_to_Text[0:first] +'at the begining  and' + UserVoiceInput_converted_to_Text[(first+1):] +'at the end'
                    else :
                        mytext = 'wrong word'

                        # Language we want to use
                    language = 'en'

                    myobj = gTTS(text=mytext, lang=language, slow=False)

                    myobj.save("output.mp3")

        # Play the converted file
                    os.system("start output.mp3")
                        
            except KeyboardInterrupt:
                print('A KeyboardInterrupt encountered; Terminating the Program !!!')
                exit(0)

            except speech_recognition.UnknownValueError:
                print("No User Voice d+etected OR unintelligible noises detected OR the recognized audio cannot be matched to text !!!")
        break
    default:
                # Import the Gtts module for text
        # to speech conversion
        from gtts import gTTS

        # import Os module to start the audio file
        import os

        mytext = 'sorry, please choose a valid option'

        # Language we want to use
        language = 'en'

        myobj = gTTS(text=mytext, lang=language, slow=False)

        myobj.save("output.mp3")

        # Play the converted file
        os.system("start output.mp3"


