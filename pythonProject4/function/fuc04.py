import datetime


def get_list(food):
    if food=="korea":
        data=['냉면','오미자차','맡빙수']
    elif food=="japan":
        data = ['우동', '생면']
    else:
        data = ['라면', '커피']

    return data


def get_day():
    return datetime.datetime.today()
def get_day2():

    today=datetime.datetime.today()
    return today.month, today.hour


if __name__ == '__main__':
    #return은 여러개일수있다.
    #하나의 변수에 리턴값을 넣어주면 tuple로 묶어준다.>>리스트와비슷
    result3 = get_day2()
    a,_ = get_day2()
    print(a)
    print(result3[1])
    result2=get_day()
    result=get_list('japan')
    print(result2.month,":",result)