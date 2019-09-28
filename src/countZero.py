

def countZero(n):
    m = 10
    num = 0
    while n % m == 0:

        num += 1
        n = int(n // m)
        #print("loop:", n)

    return num


def countZero2(n):
    s = str(n)
    arr = list(s)

    i = len(s) - 1
    num = 0
    while arr[i] == '0':
        i -= 1
        num += 1

    return num

#print(countZero2(93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000))