
try:
    file = open('member.txt','w')

    for _ in range(3):
        name = input('당신의 이름은')
        age = input('당신의 나이는')
        tel = input('당신의 연락처는')
        print("---------------------")
        data= name+","+age+","+tel+"\n"
        file.write(data)

except NameError:
    print("해당 이름의 파일을 찾을수없음")
except FileNotFoundError:
    print("해당 파일을 찾을수없음")
except IOError:
    print("읽고 쓰는데 문제가 생김")
except:
    print("파일을 처리하는데 문제가 생겼음")
finally:
    try:
        file.close()
    except:
        print("파일 닫는데 문제가 생김")