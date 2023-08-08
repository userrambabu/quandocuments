import gtts as gt
import os
from playsound import playsound
Tamil="விஷால் எங்கிருந்தாலும் வரவும் இடைவேளைக்கு பைதான் புலி"
tts=gt.gTTS(text=Tamil,lang='ta')
tts.save("DO.mp3")
playsound("DO.mp3")
os.remove("DO.mp3")
