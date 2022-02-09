# You are given two sorted lists of size m and n.
# Give an O(log m + log n) time algorithm for computing the kth smallest element
# in the union of the two lists.
import random
import numpy as np


def kth_element(arr1, arr2, k):
    if len(arr1) == 0:
        return arr2[k-1]
    elif len(arr2) == 0:
        return arr1[k-1]
    if arr1[k//2-1] >= arr2[k//2-1]:
        return kth_element(arr1[:k//2], arr2[k//2:], k-k//2)
    else:
        return kth_element(arr1[k//2:], arr2[:k//2], k-k//2)


# test case 1
a = sorted(np.random.randint(10, size=5))
b = sorted(np.random.randint(10, size=5))
print('arr1 is', a)
print('arr2 is', b)
print('the 5th number is', kth_element(a, b, 5))

# test case 2
print('\n')
a1 = sorted(np.random.randint(100, size=10))
b1 = sorted(np.random.randint(100, size=10))
print('arr1 is', a1)
print('arr2 is', b1)

print('the 6th number is', kth_element(a1, b1, 6))

# test case 3
print('\n')
a2 = sorted(np.random.randint(100, size=10))
b2 = sorted(np.random.randint(100, size=10))
print('arr1 is', a2)
print('arr2 is', b2)

print('the 10th number is', kth_element(a2, b2, 10))
