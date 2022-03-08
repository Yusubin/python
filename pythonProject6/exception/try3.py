

try:
    food = ['coffee', 'water']
    food[2] = 'juice'
except IndexError:
    food[0] = 'juice'
except ZeroDivisionError:
    print("특별히 예외처리할 내용없음")
except:
    pass
finally:
    print("필요한 예외처리를 하였음")
print(food)