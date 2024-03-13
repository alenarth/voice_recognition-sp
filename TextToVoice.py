import pyttsx3

def convertVoz(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()
    
convertVoz("Olá, meu nome é Arthur!")
convertVoz("Hi my name is Arthur")
