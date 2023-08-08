from PIL import Image
import fitz
import pyttsx3# import pyttsx3.pymupdf
doc=fitz.open("DEVOPS pdf.pdf")
text=""
for page in doc:
    text+=page.get_text()
    print(text)

    engine=pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
