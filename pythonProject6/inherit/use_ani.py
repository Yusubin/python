# from animal import animal
from inherit.animal import *

d1 = Dog('m')
d1 = Dog('m2')
a1 = Animal('hong')
a2 = Animal('happy')
d1.speak()
d1.move()

du1=Duck('d')
du1.move()
du1.speak()

print(a1.name)
print(a2.name)

a1.move()
a1.move()
a1.move()

