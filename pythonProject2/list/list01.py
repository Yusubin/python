food=[] #list

food.append('커피')
food.append('라면')
food.append('짜장면')
food[0]='라떼'
print(len(food))

print(food)

# del food[1]
# print(food)

# food.remove('라떼')

food.reverse()
# food.pop()

for x in food:
    print(x, end=' ')

print()
for i in range(len(food)):
    print(food[i], end=' ')
