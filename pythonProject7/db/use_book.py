#북마크 테이블에 대한 crud기능을 처리하고싶음import pymysql
import sys
from tkinter import messagebox

from db.dao import *
# from  패키지 import 모듈
# from  패키지.모듈명 import 함수명, 클래스명, *

if __name__ == '__main__':
    choice = input(" 1) CREATE   2)UPDATE   3) DELETE  4)READ  5) READALL: ")
    if choice == "1":
        id = input("ID : ")
        name = input("NAME : ")
        url = input("URL : ")
        img = input("IMG : ")

        vo=(id, name, url, img)
        create(vo)

    elif choice == "2":
        id = input("ID : ")
        name = input("NAME : ")
        vo = (name, id)
        update(vo)

    elif choice == "3":
        id = input("DELETE ID : ")
        delete(id)

    elif choice == "4":
        id = input("READ ID : ")
        one = read(id)
        print("""
                  --------------------------------------------------------------------
                  검색 결과
                  --------------------------------------------------------------------
                  ID | NAME |                 URL                 |        IMG
                  --------------------------------------------------------------------
                  """)
        print("                   %s   %s      %s                     %s" % one)

    elif choice == "5":
        all = readall()
        print("""
           --------------------------------------------------------------------
           검색 결과
           --------------------------------------------------------------------
           ID | NAME |                 URL                 |        IMG
           --------------------------------------------------------------------
           """)
        for i in all :
            print("           %s   %s      %s                     %s" %i)
    else:
        sys.exit(0)