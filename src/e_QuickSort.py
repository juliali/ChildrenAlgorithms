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


def quick_sort(arr, low, high):
    ###TODO
    p = partition(arr,low,high)
    if p >= 0:
        quick_sort(arr, low, p-1)
        quick_sort(arr, p+1, high)
    ###
    return


if __name__ == "__main__":

    arr1 = [6, 2, 1, 3, 7, 9, -2, 0, 8, 12]
    quick_sort(arr1, 0, len(arr1) - 1)
    print(arr1)
