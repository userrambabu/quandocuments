import pyttsx3

with open('do.txt') as c:
    text=f.readlines()
    print(text)

    engine=pyttsx3.init("sapi5")
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    newVoiceRate=120
    engine.setProperty('rate',newVoiceRate)
    engine.say(text)
    engine.runAndWait()
    
