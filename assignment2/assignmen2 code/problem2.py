# solution1:
import heapq


def partition(arr, low, high):
    i = (low-1)		 # index of smaller element
    pivot = arr[high]	 # pivot
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)


def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)


def new_list(arr):
    quickSort(arr, 1, len(arr)-1)
    b = []
    previous = None
    for i in arr:
        if i != previous:
            b.append(i)
        previous = i
    return b


print('Use quick sort and add distinct number into a new list')
arr = [1, 2, 4, 5, 7, 8, 8, 8, 8, 8, 8, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]
quickSort(arr, 1, len(arr)-1)
print(new_list(arr))


print("another method-----------\n",)
print('push all item in a into a heap, and pop one by one, add distinct item into a new list')
arr2 = [2, 6, 7, 8, 9, 1, 9, 9, 9, 2, 2, 8, 8]
heap = heapq.heapify(arr2)
print(arr2)


def heap_remove_duplicates(iterable):
    h = []
    for value in iterable:
        heapq.heappush(h, value)
    result = []
    previous = 0
    for i in range(len(h)):
        now = heapq.heappop(h)
        if now != previous:
            result.append(now)
        previous = now
    return result


print(heap_remove_duplicates(arr2))
