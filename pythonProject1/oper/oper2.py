#비교연산자.
#==, !=, >=, >,<=,<

import tkinter.messagebox as box
saved_id='root'
data_id=input('당신의 id>>')
result=saved_id==data_id
print(result)

if(result):
    print("로그인성공")
    box.showinfo('result', '로그인성공')