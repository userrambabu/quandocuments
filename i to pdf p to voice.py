from PIL import Image#import pillows
import fitz
import pyttsx3#import pyttsx3
import ocrmypdf#import ocrmypdf

#must import camelot.pypdf2 and some more packages and install tesseract and ghostscript

#image to scanned pdf
image_1=Image.open(r'c:\Images\1.png')
image_2=Image.open(r'c:\Images\2.png')
image_3=Image.open(r'C:\Images\3.png')

im_1=image_1.convert('RGB')
im_2=image_2.convert('RGB')
im_3=image_3.convert('RGB')

image_list=[im_2,im_3]

im_1.save(r'C:\Images\do.pdf',save_all=True,append_images=image_list)
image_1=Image.open(r'C:\Images\3.png')
im_1=image_1.convert("RGB")

#pdf to full text pdf
def ocr(file_path,save_path):
    ocrmypdf.ocr(file_path,save_path,skip_text=True)

    ocr("doo.pdf","doo2.pdf")

    #fulltext pdf to voice output
    doc=fitz.open('doo2.pdf')
    text=""
    for page in doc:
        text+=page.get_text()
        print(text)
        engine = pyttsx3.init()
        newVoiceRate = 120
        engine.setProperty('rate',newVoiceRate)
        engine.say(text)
        engine.runAndWait()                              
        




