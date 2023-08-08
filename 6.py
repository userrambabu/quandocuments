import pyttsx3# import pyttsx3

engine = pyttsx3.init()
newVoiceRate = 110
engine.setProperty('rate',newVoiceRate)
engine.say("Welcom to training attend students")
engine.runAndWait()
