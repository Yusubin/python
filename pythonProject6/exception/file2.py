
try:
    test_file = open('member.txt','r')
    lines=test_file.readlines()
    data = lines[0].split(",")
    print("이름     나이     연락처")
    print("-----------------------------")
    for li in lines:
        one=li.split(",")
        print(one[0]+"     "+one[1]+"     "+one[2] )
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
        test_file.close()
    except:
        print("파일 닫는데 문제가 생김")
    test_file.close()
