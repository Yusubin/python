#space
s1='    samsung'
s2='            samsung'
s3='       samsung'
s4='          samsung\n'


print(s1.strip())
print(s2.strip())
print(s3.strip())
print(s4.strip())


print(s4.strip()=='samsung')

num_str=['10','20','30',' 40']

for one in num_str:
    print(int(one))