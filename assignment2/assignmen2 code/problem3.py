arr = [4, 1, 2, 36, 5, 21, 8, 13, 11, 20, 5]


# range range(start, stop, step)


def partition(arr, low, high):
    i = low-1
    pi = arr[high]
    for j in range(low, high):
        if arr[j] <= pi:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    # print(arr)
    return i+1


def find_median(arr, n):
    if len(arr) == 1:
        return arr[0]
    low = 0
    high = len(arr)-1
    if low < high:
        pi = partition(arr, low, high)
        print(pi)

        if n >= pi:
            print(arr[pi:])
            find_median(arr[pi:], n-pi)

        if n <= pi:
            print(arr[:pi+1])
            find_median(arr[:pi], n)


print(find_median(arr, 8))
