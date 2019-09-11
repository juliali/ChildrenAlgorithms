from utilities import swap


def partition(arr, low, high):
    if low >= high:
        return -1

    pi = low
    li = low + 1
    ri = high

    while ri >= li:
        if arr[li] > arr[pi]:
            swap(arr, ri, li)
            ri -= 1
        else:
            li += 1

    pi = li - 1
    swap(arr, low, pi)

    return pi


def quick_sort(arr):
    ### TODO ADD Logic

    ###
    return


if __name__ == "__main__":

    arr1 = [6, 2, 1, 3, 7, 9, -2, 0, 8, 12]
    print(quick_sort(arr1))
