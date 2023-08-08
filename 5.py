import pyttsx3
text_to_speech=pyttsx3.init()
while True:
    speech=input("Enter the text you want to convert into speech;--")
    text_to_speech.say(speech)
    text_to_speech.runAndWait()
    
