from tkinter import *
from tkinter import messagebox

def plus():
    vvar1 = var1_entry.get()
    vvar2 = var2_entry.get()
    print(type(vvar1))
    result = int(vvar1) + int(vvar2)
    messagebox.showinfo("결과", str(result))

def minus():
    vvar1 = var1_entry.get()
    vvar2 = var2_entry.get()
    result=int(vvar1)-int(vvar2)
    messagebox.showinfo("결과", str(result))
def multi():
    vvar1 = var1_entry.get()
    vvar2 = var2_entry.get()
    result = int(vvar1) * int(vvar2)
    messagebox.showinfo("결과", str(result))
def div():
    vvar1 = var1_entry.get()
    vvar2 = var2_entry.get()
    result = int(vvar1) / int(vvar2)
    messagebox.showinfo("결과", str(result))

def reset():
    var1_entry.delete(0,END)
    var2_entry.delete(0,END)
w=Tk()
w.geometry("500x500")
var1=Label(w, text= '수를 입력하세요', font=('궁서',10))
var2=Label(w, text= '두번째 수를 입력하세요', font=('궁서',10))
var1_entry=Entry(w, font=('궁서', 10), bg='blue',fg='white')
var2_entry=Entry(w, font=('궁서', 10), bg='blue',fg='white')
plus=Button(w, text='+', font=('궁서', 10), bg='yellow', command=plus)
minus=Button(w, text='-', font=('궁서', 10), bg='yellow', command=minus)
multi=Button(w, text='x', font=('궁서', 10), bg='yellow', command=multi)
div=Button(w, text='/', font=('궁서', 10), bg='yellow', command=div)
rs=Button(w, text='E', font=('궁서', 10), bg='yellow', command=reset)
var1.pack() #라벨을 w에 넣어줌
var2.pack() #라벨을 w에 넣어줌
var1_entry.pack()
var2_entry.pack()
plus.pack()
minus.pack()
multi.pack()
div.pack()
rs.pack()
w.mainloop()