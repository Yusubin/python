import random

from worker import *
if __name__ == '__main__':
    # 2. 직원을 채용할 때마다 지금까지의 직원수를 프린트

    # hubo=[{"name":'홍길동', "age":24, "gender":"남"},{"name":'김길동',"age": 23, "gender":"여"},{"name":'박길동', "age": 28, "gender": "남"},{"name":'이길동', "age": 21, "gender": "남"},{"name":'장길동',"age": 29,"gender": "여"}]
    gender_list = ['남', '여']
    for i in range(1000):
        age_rand = random.randint(20, 35)
        gender_choice = random.choice(gender_list)
        Worker('홍길동', age_rand, gender_choice)

    w1 = Worker('홍길동', 24, "남")
    print("채용:", w1)
    print(Worker.count_person)
    w2 = Worker('김길동', 23, "여")
    print("채용:", w2)
    print(Worker.count_person)
    w3 = Worker('박길동', 28, "남")
    print("채용:", w3)
    print(Worker.count_person)
    w4 = Worker('이길동', 21, "남")
    print("채용:", w4)
    print(Worker.count_person)
    w5 = Worker('장길동', 29, "여")
    print("채용:", w5)
    print(Worker.count_person)
# 1. 전체 직원에 대한 정보를 프린트
    print(w1,"|",w2,"|",w3,"|",w4,"|",w5)
# 3. 직원 나이의 평균 프린트
    print("평균나이:", (Worker.count_age/Worker.count_person))
# 4. 성별 직원수 프린트
    print("남:", Worker.man_count)
    print("여:", Worker.woman_count)