# This is document for assignment 2

divide and conque video,

**_important_**
https://www.youtube.com/watch?v=11V7Ik0IBHU

# problem 1

## solution 1

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

> Output of Solution1
> ![output](https://github.com/zyune/CS5800_algorithem/blob/main/assignment2/screenshoot/p1s1.png)

## solution 2

- This solution uses hashtable to solve the problem which is much easy to understand and the time complexity is O(n)

- We create a dictionary memo{} to store the number we had went through, key is the number, value is the frequency of the number.
- If we had not went through the number before, add it in the memo{} ,and set the value of key to 1.if we had went through it the value of the key +1.

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

> Output of Solution2
> ![output](https://github.com/zyune/CS5800_algorithem/blob/main/assignment2/screenshoot/p1s2.png)

# problem 2

## solution1

- First, use quicksort to sort the array.
- Second, create a new list b.
- Third, iterate list a. if the n item of list a doesn't equal to the previous item, add the item into list b
  > the time complixity of this is T(n)=T(nlogn)+T(n), because n is smaller than nlogn, so O(n log n).

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

> # output of solution 1
>
> ![output](https://github.com/zyune/CS5800_algorithem/blob/main/assignment2/screenshoot/p2s1.png)

## solution2

- This uses heap to solve the problem. The time complicity of heap sort is nlogn.
- This solution used heapq which is a python module
- Use a for loop to pop the top element of the heap, if now is not equal to previous ,add the number into a new list b

```python
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

```

> output of solution2
> ![output](https://github.com/zyune/CS5800_algorithem/blob/main/assignment2/screenshoot/p2s2.png)

# problem 3

## solution 1

- The base case is when len(arr) is 1, Then there are only one number in the array, Then this number must be the number we are looking for.
- how to do the split? we use the last number of the list as the pivot, and we do the partition first. The left halves of pivot are smaller than pivot the right half of pivot are bigger than pivot.
- We check if n is bigger or smaller than pivot. If n is bigger than pivot, we recurse the find_median(), the inputs will be the right half of array and (n-pivot). If n is smaller or equal than pivot, we recurse the find_median(), the input will be the left side of array and n
- The return value of the function has some problem, but I can see the result through print

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

> output of solution1
> ![output](https://github.com/zyune/CS5800_algorithem/blob/main/assignment2/screenshoot/p3s1.png)

## solution 2

- The use of heap to solve the smallest/ biggest is very easy to figure out. Because the top element of a max heap is the biggest , and the top element of min heap is the smallest

I solved the same question on leetcode on Dec 6th 2021, where I use heap to solve the problem.https://github.com/zyune/data_structure_python/blob/main/heap/Medianfinder.py

```python
class MedianFinder:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        if not self.max_heap or num < -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)
        if len(self.max_heap) > len(self.min_heap) + 1:
            heappush(self.min_heap, -heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heappush(self.max_heap, -heappop(self.min_heap))

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] - self.max_heap[0]) / 2
        return -self.max_heap[0]
```
