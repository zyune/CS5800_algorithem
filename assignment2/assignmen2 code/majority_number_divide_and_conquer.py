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


arr = [1, 2, 4, 5, 7, 8, 8, 8, 8, 8, 8, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]
quickSort(arr, 1, len(arr)-1)
print(arr)
count = 0
max_count = 0
previous = arr[0]
for i in range(len(arr)):

    if i == previous:
        count += 1
    else:
        count = 1
    if count > max_count:
        max_count = count
    previous = i
print(max_count)

# def count_majority_number(arr):
#     return 0

# def majority_number(arr):
#     if left == right:
#         return left
#     pi=len(arr)//2
#     left_majority = majority_number(arr[:pi])
#     right_majority = majority_number(arr[pi:])
#     if left_majority==right_majority:
#         return left_majority
# def compare(arr,left,right):
#     if left==right:
#         return left
#     pi=len(arr)//2
#     compare(arr, left, pi)
#     compare(arr, pi, right)
# def count_frequecy(arr):
#     count=1
#     for i in arr:
# int countFrequency(int X[], int l, int r, int majority)
# {
#     int count = 0
#     for (int i=l
#          i <= r
#          i=i + 1)
#     {
#         if (X[i] == majority)
#         count = count + 1
#     }
#     return count
# }
arr = [1, 2, 3, 4, 5, 6, 6, 7, 7, 8, 8, 8, 9]
# pi = len(arr)//2
# left = arr[:pi]
# right = arr[pi:]
# print(left)
# print(right)
# majority_number(arr)


def countFrequency(arr, left, right, majority):
    count = 0
    for i in range(left, right):
        if arr[i] == majority:
            count += 1
    return count


# int getMajorityElement(int X[], int n)
# {
#     return getMajority(X, 0, n-1)
# }
def getMajorityElement(arr, n):
    return getMajority(X, 0, n-1)

# int getMajority(int X[], int l, int r)
# {
#     if (l == r)
#     return X[l]

#     int mid = (r - l)/2 + l
#     int leftMajority = getMajority(X, l, mid)
#     int rightMajority = getMajority(X, mid + 1, r)

#     if (leftMajority == rightMajority)
#     return leftMajority

#     int leftCount = countFrequency(X, l, r, leftMajority)
#     int rightCount = countFrequency(X, l, r, rightMajority)

#     if(leftCount & gt
#        rightCount)
#     return leftCount
#     else
#     return rightCount
# }


def getMajority(arr, left, right):
    if(left == right):
        return arr[left]
    pi = (left+right)//2
    leftMajority = getMajority(arr, left, pi)
    rightMajority = getMajority(arr, pi+1, right)
    if leftMajority == rightMajority:
        return leftMajority
    leftCount = countFrequency(arr, left, right, leftMajority)
    rightCount = countFrequency(arr, left, right, rightMajority)
    if leftCount > rightCount:
        return leftCount
    else:
        return rightCount
