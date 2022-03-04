def spring(a,b):
    print(a,"월에",b, "에 가요!")

def summer(a,b):
    price=10000
    if b==6: price=price-2000
    elif b==7: price=price-1000
    elif b>8: price=price+2000
    print(b,"월에",a, "에 가는 비용은",price,"원입니다")

