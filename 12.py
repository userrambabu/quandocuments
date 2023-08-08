import sys
import time
import logging
import pyttsx3
from watchdog.observers import Observer#import watchdog==2.3.1
from watchdog.events import LoggingEventHandler

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
newVoiceRate = 130
engine.setProperty('rate',newVoiceRate)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(message)s')
    
                        
    path =r"C:\Users\Rambabu\Downloads"
    event_handler = LoggingEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    
    observer.start()
    speak("Monitoring ")
    print(format)
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
                observer.stop()
                print("Done")
                observer.join()
