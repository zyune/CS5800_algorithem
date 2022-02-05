# This is document for assignment 2

I will never use latex again in my life

> this is my quote

> # this is my really big quote

**bold sentense**

# problem 1

##solution 1

The spirit of solution 1 for problem 1 is divide and conquer.

- the base case is left=right , left and right are two pointers.when left=right, left and right are pointing the same index of the list which means we are on the least case, no more dividing.
- the getMajority() first deivide the list in to two part, and try to get the majority number in left half and right half. Then use the countFrequency() to get the frequencies of two number in this array separately. Why it works? Because as long as one of the number show up more than len(arr)/2 times, it show up more than either len(arr[:pi])/2 times on the left half or en(arr[pi:])/2 times on the right half
- some website gives me idea of how to do the solution:
  https://www.enjoyalgorithms.com/blog/find-the-majority-element-in-an-array

```python
def getMajorityElement(arr, n):
    return getMajority(arr, 0, n-1)


def countFrequency(arr, left, right, majority):
    count = 0
    for i in range(left, right):
        if arr[i] == majority:
            count += 1
    return count


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
        return leftMajority
    else:
        return rightMajority
```

![output]{https://github.com/zyune/CS5800_algorithem/blob/main/assignment2/screenshoot/Screen%20Shot%202022-02-05%20at%202.49.13%20PM.png}
##solution 2
This solution uses hashtable to solve the problem which is much easy to understand and the time complexity is O(n)

```python
def make_a_hashtable(arr):
    memo = {}
    for i in arr:
        if i not in memo:
            memo[i] = 1
        else:
            memo[i] += 1
    return memo


def majority_number(arr):
    memo = make_a_hashtable(arr)
    max = 0
    max_key = ''
    # this is how we iterate through dict.items() to access the keys and values of a dictionary.
    for i, j in memo.items():
        if j > max:
            max = j
            max_key = i
    return max_key

```

# problem 2

```python
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

```

# problem 3

```python
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

        if n > pi:
            print(arr[pi:])
            find_median(arr[pi:], n-pi)

        if n <= pi:
            print(arr[:pi+1])
            find_median(arr[:pi], n)
```
