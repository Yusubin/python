data="감자고구마양파"
print(len(data))
print(type(data))
potato=data[0:2]#[:2]
yang=data[5:7]#[5:]
last=data[2:5]
print("마지막 글자 %s" % last)
print("첫번째 단어 {0} 두번재 단어 {1} 세번재 단어 {2}".format(potato,yang,last))

data2="생수커피"
data3=data+data2
print(data3)
# print('----------------------------')
# first=data[2]
# last=data[4]
# #포맷팅
# print("첫번째 글자 %s 마지막 글자 %s" % (first, last))
# print("첫번째 글자 {0} 마지막 글자 {1}".format(first,last))
# print("첫번째 글자 {f} 마지막 글자 {l}".format(f=first,l=last))
# our=(first,last ) #읽기전용 튜플
# print("첫번째 글자 {o[0]} 마지막 글자 {o[1]}".format(o=our))