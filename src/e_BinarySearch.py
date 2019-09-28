
def binary_search(arr, tn):
    ### TODO ADD Logic
    low = 0
    high = len(arr)-1
    while low <= high:
        m = int((high-low)/2)+low
        if arr[m] == tn:
            return m
        else :
            if arr[m] < tn:
                low = m+1
            else:
                high = m-1
    ###
    return -1


if __name__ == "__main__":

    arr1 = [1, 3, 5, 7, 8, 9, 12, 17, 23, 29, 33, 45, 50]
    index = binary_search(arr1, 5)

    print(index)

