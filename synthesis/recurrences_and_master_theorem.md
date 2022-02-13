# 3 **Recurrences and Master Theorem**

## 3.1 **Recurrences**

What is a recurrence? Some one says it is equal to recurrence relation. Even dasgupta will use the word 'recurrence' to represent recurrence relation.I don't want to mess recurrence with recurrence relation. For me recurrence is a process that when we  the recurse the funtion(go deeper and do the same process as the upper level). 
The most common word I see is recurrence relation. I didn't see a exact definition for recurrence relation in dasgupta, so I go for google.
A recurrence relation is an equation that defines a sequence based on a rule that gives the next term as a function of the previous term(s) such as $T(n)=2T(n/2)+O(n)$ or any form that describe the relationship between $T(n)$ and $T(n') (n'< n)$

This is a sentense in dasgupta
**_Their running time can therefore be captured by the equation T (n) = aT (⌈n/b⌉) + O(nd). We next derive a closed-form solution to this general recurrence so that we no longer have to solve it explicitly in each new instance._**
The embodiment of a closed-form solution in the code is the base case.

### **exercise:**

<your write up goes here>

### **solution:**
<your write up goes here>

##3.2 **Master Theorem**
In the book of Dasgupta, it only give master theorem2 
![image_of_master_theorem](/assets/master_theorem.png)
***What is a, what is the embodiment of a in code?***
In dasgupata, it is called branching factor.The definition of Branching factor is is the number of children at each node. It's really hard to undersyand.Actually, The most east way to understand a is that a is the number of recursive calls in one level of recursive call. **Take the quick sort code as an example**. It call quickSort() recursely twice in one level of the function so $a=2$.

***code sample1***
```python
def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1) #first time a=1
        quickSort(arr, pi+1, high) #second time a=2
```
Another example is the presocode of $Figure 2.1$ in Dasgupta. It call multiply recursely for 3 times in function. So a=3

***code sample2***
```python
function multiply(x, y)
Input: Positive integers x and y, in binary Output: Their product
n = max(size of x, size of y) if n = 1: return xy
xL, xR = leftmost ⌈n/2⌉, rightmost ⌊n/2⌋ bits of x yL, yR = leftmost ⌈n/2⌉, rightmost ⌊n/2⌋ bits of y
P1 =multiply(xL,yL) # first time a=1
P2 =multiply(xR,yR) # second time a=2
P3 =multiply(xL +xR,yL +yR) #third time a=3
return P1 ×2n +(P3 −P1 −P2)×2n/2 +P2
```
***What is b, what's the embodiment of b in code?***
b is  how the data gets cut into. At first I was a little bit confused about b and a. Until I got into the code. Let's the the code in **code sample1**, it cut the array into two part when it call the recursive function which is ```arr[low:pi-1]``` and ```arr[pi+1:high]```. So the $b=2$
```python
    quickSort(arr, low, pi-1) #first time a=1
    quickSort(arr, pi+1, high) #second time a=2
```

If we cut the arr into ```arr[:pi1],arr[pi1:pi2] and arr[pi2:]``` Then $ b=3$
***What is $O(n^d)$, what's the embodiment of $O(n^d)$ in code.***
Actually, $O(n^d)$ identify how long it takes to put all branch back again.We cannot find a exact embodiment in code.
![picture of master theorem](/assets/picture_of_master_theorem.png) 

### **exercise:**
At the top level we use n - 1 comparisons and then have to sort the buckets A< and A> which have approximately (n - 1)/2 elements each. To make the arithmetic simpler, let’s say that we use n comparisons and end up with two buckets of size n/2.
Please give the Derived formula for the best case for quicksort.
Let f(n) denote the number of comparisons needed by Quicksort in the best case. We then have the recurrence relation:
f(n) = n + 2f(n/2)
### **solution:**

## 3.3 **using Master Theorem to analyze a recursive algorithm**
```python
def partition(arr, low, high):
    i = (low-1)
    pivot = arr[high]
    for j in range(low, high):
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
```
In best case, the size of the largest bucket goes down by a factor of 2 each time.
At the top level we use $n - 1$ comparisons and then have to sort the buckets A< and A> which have approximately $(n - 1)/2$ elements each. To make the arithmetic simpler, let’s say that we use n comparisons and end up with two buckets of size $n/2$.
Let f(n) denote the number of comparisons needed by Quicksort in the best case. We then have the recurrence relation: $T(n) = n + 2T(n/2)$
a=2,b=2,d=1 because $log{_b}{a}=d=1$, so $T(n)=n^dlog(n)$
***If we write it in close-form***
$T(n) = 2T(n/2)+n$
$= 2[2T(n/4)+cn/2]+cn = 4T(n/4)+2cn $
$= 4[2T(n/8)+cn/4]+2cn = 8T(n/8)+3cn$
$= 8[2T (n/16) + cn/8] + 3cn = 16T (n/16) + 4cn.$
the general term is $T(n) =2^kT(n/2^k) + kn$
plug in  $k = log{_2}{n}$ ,then $T(n)=nT(1)+nlog{_2}{n}=O(nlog{n})$

### **exercise:**
Use Master Theorem to analyze
```python
def kth_element(arr1, arr2, k):
    if len(arr1) == 0:
        return arr2[k-1]
    elif len(arr2) == 0:
        return arr1[k-1]
    if arr1[k//2-1] >= arr2[k//2-1]:
        return kth_element(arr1[:k//2], arr2[k//2:], k-k//2)
    else:
        return kth_element(arr1[k//2:], arr2[:k//2], k-k//2)
```
In this function a=2,b=2 and the best case for f(n) is log

### **solution:**
- In this code we have two array.  Every time I call the function recursely only once, so a=1
- I divide two list which are arr1 and arr2 into two parts separately. We should treat the two lists as a whole, so I still divide the whole data into two parts
- $f(n)=O(1)$, here because I only made 1 comparison here which is  $arr1[k//2-1] >= arr2[k//2-1]$
- recurrence relation for this code is $T(n)=T(n/2)+O(1)$
- In the recurrence relationship $a=1,b=2,d=0$
- because $log{_b}{a}=log{_2}{1}=0$
- so $T(n)=O(logn)$