
hobby={10:['game','picture'], 20:['tour','run','band']}
hobby2={10:{'아침':'game','저녁':'picture'}, 20:['tour','run','band']}
hobby3=[
    {10:{'아침':'game','저녁':'picture'}},{20:{'아침':'coding','저녁':'sssss'}}
]

#10대의 취미목록 프린트
s100=hobby3[0]
s1000=s100[10]
s10000=s1000['저녁']
print(s10000)
print(hobby[10])
# #20대의 취미목록 프린트
# print(hobby[20])
# #20대의 취미목록 카운트
# print(len(hobby[20]))
# food={'아침':'토스트','점심':'한정식','저녁':'스프' }
# print(food['아침'])
# food['아침']='커피'
# print(food)
# food['간식']='쿠키'#값을 추가할때
# print(food)
#
# del food['간식']
# print(food)
#
# for key in food:
#     print(key,':',food[key]) #키만가지고온다.
#
# dict1={100:'hong', 200:'kim'}
# print(dict1[100])
#
#
# for jey in dict1:
#     print(jey, ":", dict1[jey])
# key_list =dict1.keys()
# key_list2 =list(key_list)
# print(key_list2)
#
# value_list =dict1.values()
# value_list2 =list(value_list)
# print(value_list2)
#
# print(dict1.get(100))
# print(100 in dict1) #dict1에 100이 잇나요 (True/False)
#
# if 500 in dict1:
#     print('500회원이 존재합니다')
# else:
#     print('존재하지 않습니다')