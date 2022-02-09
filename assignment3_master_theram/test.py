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


a = [2, 4, 5, 8, 9, 10, 14, 19, 23, 80]
b = [3, 4, 6, 9, 10, 22, 30]

print(kth_element(a, b, 6))


print(random.randint(1, 10))

a1 = sorted(np.random.randint(100, size=10))
a2 = sorted(np.random.randint(100, size=10))
print(a1)
print(a2)
