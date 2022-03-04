from function.exam.room import Tv

tv1 = Tv()
tv2 = Tv()

tv1.color = "blue"
tv1.ch = 73
tv1.tel = "SKT"
tv2.color = "RED"
tv2.ch = 121
tv2.tel = "LG U+"

print("tv1:", tv1)
print("tv2:", tv2)
tv2.channel(42)