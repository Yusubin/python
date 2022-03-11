import sys
from db.member_dao import *

if __name__ == '__main__':
    choice = input(" 1) 회원가입   2)회원탈퇴   3) 회원정보  4)로그인: ")
    if choice == "1": #회원가입
        id = input("ID : ")
        pw = input("PW : ")
        name = input("NAME : ")
        tel = input("TEL : ")

        vo=(id, name, pw, tel)
        create(vo)

    elif choice == "2":
        id = input("DELETE ID : ")
        delete(id)

    elif choice == "3":
        id = input("READ ID : ")
        one = read(id)
        print(
            """---------------------------------------
검색 결과
---------------------------------------""")
        if one != None:
            print("""ID  |  PW  |    NAME    |     TEL
---------------------------------------""")
            print("%s   %s     %s    %s" % one)
        else:
            print("검색결과 없음.")

    elif choice == "4":
        id = input("ID : ")
        pw = input("NAME : ")
        vo = (id, pw)
        print(login(vo))
    else:
        sys.exit(0)