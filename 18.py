import requests#import requests==2.28.1
import json
import pyttsx3#import
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
newVoiceRate = 130
engine.setProperty('rate',newVoiceRate)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

api_key = "c71021a1f238448c8fdd1fa48e5c64e9"

base_url = "https://newsapi.org/v2/top-headlines"
a="Description"
country_code="in"
complete_url = base_url + "?country=" + country_code + "&apiKey=" + api_key
response = requests.get(complete_url)
data = response.json()
till = "Description: "
if data["status"] == "ok":
    articles = data["articles"]
    for article in articles:
      print("Title: " + article["title"])
      print("Description:")
      print( article["description"])
      print("-" * 50)
      speak("Title: " + article["title"])
      speak("Description:")
      speak( article["description"])
      speak("-" * 50)
else:
      print("Error getting news: " + data["message"])
