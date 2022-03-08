# try:
#     test_file = open('test.txt','r')
#     lines=test_file.readlines()
#     for line in lines:
#         print(line)
# except NameError:
#     print("해당 이름의 파일을 찾을수없음")
# except FileNotFoundError:
#     print("해당 파일을 찾을수없음")
# except IOError:
#     print("읽고 쓰는데 문제가 생김")
# except:
#     print("파일을 처리하는데 문제가 생겼음")
# finally:
#     try:
#         test_file.close()
#     except:
#         print("파일 닫는데 문제가 생김")
#     test_file.close()
#

#램에 만들어진 connection을 담당하는 stream객체를 메모리에서 지우는 역할을 수행 close함수를 호출하지않으면 메모리에 꼐속 남아있어서 반드시 메모리에서 지어주어야한다.

try:
    # test_file = open('test.txt','w')
    test_file = open('test.txt','a')
    result=test_file.write('hello hi lunch\n')
    result=test_file.write('hello2 hi2 lunch2')
    print(result)
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
