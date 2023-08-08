import gtts as gt# import gtts
import os
import io
from playsound import playsound# import playsound
with open('ram.txt',encoding="utf8")as c:
    TamilText1=f.readlines()
    with open('demo.txt') as c:
        for TamilText in TamilText1:
            print(TamilText)
            gv=gt.gTTS(text=TamilText, lang='en')
            gv.save("mam.mp3")
            playsound("mam.mp3")
            os.remove("mam.mp3")
            
