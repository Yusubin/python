

#
# 내일 우산을 가지고갈지 판단해봅시다.
# 조건: 비가올까?(0:비가온다 1:비가 안온다)
#     날이 흐린가?(0:날이흐림  1:날이 안흐림)
rain_r, goormy_r = input("비가오는가?날이 흐린가?").split()


if(rain_r == 0 or goormy_r == 0):
    print("우산가지고 퇴근")
else:
    print("우산가지고가지말자...!")
    data =input('그럼뭐할까');
    print(data, "하러가야지!")