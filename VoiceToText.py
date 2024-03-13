import speech_recognition as sr

def convertVoz():
    print('Started')
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Speak')
        audio = r.listen(source)
        print("Got the Audio")
        try:
            # Use the Google Web Speech API
            text = r.recognize_google(audio)
            print(text)
        except sr.UnknownValueError:
            print("Google Web Speech could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Web Speech service; {0}".format(e))


convertVoz()