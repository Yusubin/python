subject=['영어','수학','국어','컴퓨터','과학']
term1=[100, 99, 88, 77, 30]
#2학기 점수는 1학기와 거의 동일
term2=term1.copy()

#국어점수만 66점...
term2[2]=66
term2[4]=100
print(term2)
#1학기보다 성적이 떨어진 과목은?
#1,2학기 점수가 동일한 과목은?

for i in range(len(term2)):
    if(term1[i]==term2[i]):
        print("동일한 과목", subject[i])
    elif(term1[i]>term2[i]):
        print("떨어진 과목:", subject[i])
    else:
        print("성장한 과목:", subject[i])
