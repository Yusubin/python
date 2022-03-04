
import datetime

today=datetime.datetime.today()
num = input("주민번호입력:")
gen = int(num[6])
age = num[:2]

# if (gen==2 or gen==4):
if gen in(2,4):
    gender="여자"
else: gender="남자"

if(age[0]=="0"):
    age2=2000+int(age)
else:
    age2=1900+int(age)


real=today.year-age2+1

print("성별:",gender,"| 나이:",real)