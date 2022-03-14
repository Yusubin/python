from collections import Counter

# UI구성
from tkinter import *

from openAPI.dd1 import *


def append_item():

def lookup():
    pass


w = Tk()
w.geometry("500x500")
var1 = Label(w, text='이미지 주소 입력', font=('궁서', 10))
var1_entry = Entry(w, font=('궁서', 10), bg='blue', fg='white')

append = Button(w, text='등록', font=('고딕', 10), bg='yellow', command=append_item())
lookup = Button(w, text='조회', font=('고딕', 10), bg='yellow', command=lookup())


var1.pack()
var1_entry.pack()
append.pack()
lookup.pack()

w.mainloop()