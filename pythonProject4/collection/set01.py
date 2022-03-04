jumsu_1 = {100, 99, 88, 77}
jumsu_2 = {90, 99, 88, 66}
#두학기내내 동일한 성적인 점수는?, 과목수는?
equals=jumsu_1&jumsu_2
print(equals)
print(len(equals))

# 두학기 비교했을때 1학기성적중 2학기위 다른성적은?
differ=jumsu_1-jumsu_2 #result3=jumsu_1.difference(jumsu_2)
print(differ)

#두학기동안 획득한 전체 점수목록은?
total=jumsu_1|jumsu_2 #result3=jumsu_1.union(jumsu_2)
print(total)
result3=list(total)#비파괴형함수:원본은 안바뀜
result3.sort()#파괴형함수:원본을 바꿈
print(result3)

#반환이 잇?없
result3.reverse()
print(result3)
#1학기 성적에 음악점수 50점 추가
jumsu_1.add(50)
print(jumsu_1)
#2학기성적에 음악 77, 컴푸터 100 추가
jumsu_2.update([77, 100])
print(jumsu_2)
#1학기 성적 모두삭제
jumsu_1.clear()
print(jumsu_1)