from tkinter import *
import wikipedia
from langdetect import detect_langs
from translate import Translator

def wiki():
        search = entry.get()
        answer_value = wikipedia.summary(search)
        answer.insert(INSERT, answer_value)
ak = Tk()
ak.config(bg="blue")
ak.title("Demo wikipedia")
firstframe  = Frame(ak)
entry = Entry(firstframe)
entry.pack()
button = Button(firstframe, text="search", command=wiki)
button.pack()
firstframe.pack(side = TOP)


secondframe = Frame(ak)
scrollbar = Scrollbar(secondframe)
scrollbar.pack(side=RIGHT, fill=Y)
answer =  Text(secondframe, width=75, height=30, yscrollcommand = scrollbar.set)
translator= Translator(to_lang="Vietnamese")
scrollbar.config(command=answer.yview)
answer.pack()
secondframe.pack()

ak.mainloop()
