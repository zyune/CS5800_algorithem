# This is document for assignment 2

I will never use latex again in my life

> this is my quote

> # this is my really big quote

**bold sentense**

create unorder item using '-','\*','+'

- item

* iterm

- iterm

# problem 1

- item
  - item
  - item
    $\sum_{n=1}^{10} n^2$
    $$\sum_{n=1}^{10} n^2$$
    $\lim_{x \to \infty} f(x)$
    $\displaystyle \lim_{x \to \infty} f(x)$

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

```
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
