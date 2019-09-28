def accumulate(start,end,delta):
    t = 0
    i = start
    while i <= end:

        t = t + i
        i = i + delta

    return t


s=218
e=3426
d=5
t=accumulate(s,e,d)
print(t)














































































































