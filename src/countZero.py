def countZero(n):
    m = 10
    num = 0
    while n % m == 0:
        num += 1
        n = n / m

    return num


print(countZero(1000))