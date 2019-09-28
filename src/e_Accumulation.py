from countZero import countZero2
from countZero import countZero

def accumulate(start,end,delta):
    t = 0
    i = start
    while i <= end:

        t = t + i
        i = i + delta

    return t


def mul(start,end,delta):
    t = 1
    i = start
    while i <= end:

        t = t * i
        i = i + delta

    return t

s=1
e=100
d=1
t=mul(s,e,d)
print(t)
n = countZero(t)
print(n)














































































































