from function.exam.shop import Shop

shop1 = Shop()
shop1.genre = "옷"
shop1.location = "서울"
shop1.total_count(500, 100)
shop1.total_price(5, 3000)
print(shop1)
