# Python program for implementation of Quicksort Sort

# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot


def partition(arr, low, high):
    i = (low-1)		 # index of smaller element
    pivot = arr[high]	 # pivot
    # print("now the pivot is", pivot)
    # print('low is', low)
    # print('high is', high)
    for j in range(low, high):
        #     print('i equals to', i)
        #     print('j equals to', j)
        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:  # 判断条件是 当遇到第一个比pivot小的函数的时候 i=i+1 并把 arr[i]和arr[j]交换

            # increment index of smaller element
            i = i+1
            # print(arr[j], "have been put in front, and",
            #       arr[i], "have been put behind")

            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]  # 然后把i的下一个和high像交换
    # print("-----the array changed is ", arr)
    # print('the next pivot will be', arr[i+1], 'which is located in', i+1, )
    return (i+1)

# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low --> Starting index,
# high --> Ending index

# Function to do Quick sort


def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:

        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        print(pi-1)
        print(pi+1)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)


# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
# print(arr)
n = len(arr)
quickSort(arr, 0, n-1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i])

# This code is contributed by Mohit Kumra
# This code in improved by https://github.com/anushkrishnav
