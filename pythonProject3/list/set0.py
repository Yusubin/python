# #중복을 제거하고싶을때

#
# food_list=['감자','감자','고구마','고구마','고구마','바바바바바바','볶음밥']
# food_list2=set(food_list)
# print(food_list2)
#
# food_list3=list(food_list2)
# print(food_list3)
#
# food_list4=set()
# food_list4.add('고구감')
# food_list4.add('고구감')
# food_list4.add('커피')
#
# print(food_list4)
#
#
# food_list5=list(food_list4)
# print(food_list5)

import random
number_list=set()
for _ in range(1000):
    number_list.add(random.randint(1,1001))

print(number_list)

print(len(number_list))