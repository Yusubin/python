from tkinter import *
from tkinter import messagebox


def login():
    messagebox.showinfo('제목','나를 클릭')
    id1 = id_entry.get()
    pw1 = pw_entry.get()
    if(id1=="root" and pw1=="1234"):
        messagebox.showinfo("성공", "로그인 성공")
    else:
        messagebox.showerror("실패", "로그인 실패")
w=Tk()
w.geometry("500x500")

#라벨을 하나 만들어보자
id=Label(w, text= '아이디를 입력하세요', font=('궁서',10))
pw=Label(w, text= '패스워드를 입력하세요', font=('궁서',10))
id_entry=Entry(w, font=('궁서', 10), bg='blue',fg='white')
pw_entry=Entry(w, font=('궁서', 10), bg='blue',fg='white')
b=Button(w, text='로그인처리', font=('궁서', 10), bg='yellow', command=login)

id.pack() #라벨을 w에 넣어줌
id_entry.pack()
pw.pack()
pw_entry.pack()
b.pack()


w.mainloop()