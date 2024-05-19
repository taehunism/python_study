import module

p = module.plus(3,2)
print(p)

m = module.minus(5,3)
print(m)

from module import plus
p2 = plus(4,2)
print(p2)

from module import plus, minus
p3 = plus(4,4)
m2 = minus(5,3)
print(p3, m2)

