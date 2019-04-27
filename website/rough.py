import math
from random import randint

def random_genrator(y):
    x1 = randint(65,90)
    x1 = chr(x1)
    x2 = randint(65,90)
    x2 = chr(x2)
    x3 = randint(65,90)
    x3 = chr(x3)
    x4 = randint(0,9)
    x4 = str(x4)
    x5 = randint(0,9)
    x5 = str(x5)
    x6 = randint(97,122)
    x6 = chr(6)
    x7 = randint(97,122)
    x7 = chr(x7)
    x8 = randint(65,90)
    x8 = chr(x8)
    x9 = randint(0,9)
    x9 = str(x9)
    x10 = randint(97,122)
    x10 = chr(x10)
    x = x1+x2+x3+x4+y+x5+x6+x7+x8+x9+x10
    return x

y=random_genrator("5")
print y
