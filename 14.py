import PyPDF2

import pyttsx3

pdffileobj=open('notes.pdf', 'rb')

pdfreader=PyPDF2.PdfFileReader(pdffileobj)

x=pdfreader.num
Pages
pageobj=pdfreader.getPage(x-1)
text=pageobj.extractText()


File1=open(r"R:\Images\\2.txt","a")
File1.writelines (text)
File1.close()
file1 = open("2.txt","r")
engine = pyttsx3.init()
engine.save_to_file(file1.read(),"converted.mp3")

engine.runAndWait()


