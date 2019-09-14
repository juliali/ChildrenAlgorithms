def r1(n):
    if n > 0:
        print(n)
        r1(n - 1)

    return


def r2(n):
    ### TODO Add Logic
    ### 修改r1()的代码，使得r2(3)的打印结果为1\n 2\n 3
    if n > 0:
        r2(n - 1)
        print(n)

    ###

    return n

if __name__ == "__main__":

    print("r1 --- ")
    r1(3)
    print("r2 --- ")
    r2(3)
