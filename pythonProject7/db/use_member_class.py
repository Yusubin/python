
import tkinter

from db.member_dao_class import MemberDAO

member=MemberDAO()
from tkinter import *
from tkinter import messagebox
def create():
    c_id = id_entry.get()
    c_pw = pass_entry.get()
    c_name = name_entry.get()
    c_tel = tel_entry.get()
    vo=(c_id, c_pw, c_name, c_tel)
    member.create(vo)
    messagebox.showinfo("회원가입", "성공")
    img1 = tkinter.PhotoImage(file='aaaa.gif')
    image.config(image=img1)
    image.image=img1
    print("SUCCESS")

def login():
    c_id = id_entry.get()
    c_pw = pass_entry.get()
    vo=(c_id, c_pw)
    re=member.login(vo)
    print(re)
    messagebox.showinfo("로그인", re)
    if(re == "로그인 성공"):
        img1 = tkinter.PhotoImage(file='aaaa.gif')
        image.config(image=img1)
        image.image = img1
    else:
        img1 = tkinter.PhotoImage(file='bbbb.gif')
        image.config(image=img1)
        image.image = img1
    print("SUCCESS")

def delete():
    c_id = id_entry.get()
    member.delete(c_id)
    messagebox.showinfo("회원탈퇴","탈퇴가 완료되었습니다.")
    img1 = tkinter.PhotoImage(file='aaaa.gif')
    image.config(image=img1)
    image.image = img1
    print("SUCCESS")

def read():
    c_id = id_entry.get()
    one = member.read(c_id)
    if one != None:
        data="""---------------------------------------\n검색 결과\n---------------------------------------\n  ID       |     PW     |       NAME        |       TEL  \n---------------------------------------\n%s   %s     %s    %s""" % one
        result.config(text=data)
    else:
        data = "---------------------------------------\n검색 결과\n---------------------------------------\n검색결과 없음"
        result.config(text=data)
    print("SUCCESS")

w=Tk()
w.geometry("300x500")
id=Label(w, text= '아이디 입력:', font=('고딕',10))
pw=Label(w, text= '패스워드 입력:', font=('고딕',10))
tel=Label(w, text= '전화번호 입력:', font=('고딕',10))
name=Label(w, text= '전화번호 입력:', font=('고딕',10))
img=tkinter.PhotoImage(file='ss.gif')
image=Label(w, image = img)

result=Label(w, text= ' ', font=('궁서',10))
name_entry=Entry(w, font=('고딕', 10), bg='blue',fg='white')
id_entry=Entry(w, font=('고딕', 10), bg='blue',fg='white')
pass_entry=Entry(w, font=('고딕', 10), bg='blue',fg='white')
tel_entry=Entry(w, font=('고딕', 10), bg='blue',fg='white')

# login=Button(w, text='+', font=('궁서', 10), bg='yellow', command=login)
create1=Button(w, text='회원가입', font=('고딕', 10), bg='yellow', command=create)
delete1=Button(w, text='회원탈퇴', font=('고딕', 10), bg='yellow', command=delete)
read1=Button(w, text='정보조회', font=('고딕', 10), bg='yellow', command=read)
login1=Button(w, text='Login', font=('고딕', 10), bg='yellow', command=login)

import sys
from db.member_dao import *
from db.member_dao_class import MemberDAO

if __name__ == '__main__':
    member= MemberDAO()
    image.pack()
    choice = input(" 1) 회원가입   2)회원탈퇴   3) 회원정보  4)로그인: ")
    if choice == "1": #회원가입
        id.pack()
        id_entry.pack()
        pw.pack()
        pass_entry.pack()

        name.pack()
        name_entry.pack()

        tel.pack()
        tel_entry.pack()

        create1.pack()

    elif choice == "2":
        id.pack()
        id_entry.pack()

        delete1.pack()

    elif choice == "3":
        id.pack()
        id_entry.pack()
        read1.pack()
        result.pack()

    elif choice == "4":
        id.pack()
        id_entry.pack()

        pw.pack()
        pass_entry.pack()
        login1.pack()
    else:
        sys.exit(0)
w.mainloop()
