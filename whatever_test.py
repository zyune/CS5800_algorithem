from collections import defaultdict
import numpy as np

i = np.random.randint(100, size=10)
print(i)
print(i[::-1])  # this is very important to reverse a list or tuple:
print('\n', 'test reverse')

# Keep in mind that reversed is a generator
# (to be discussed in some more detail later),
# so it does not create the reversed sequence until
# materialized (e.g., with list or a for loop).
arr1 = [i for i in range(10)]
print(arr1)
arr2 = reversed(arr1)
print(list(arr2))
print('\n')
# You can check if a dict contains a key using the same syntax used for checking whether a list or tuple contains a value:
d1 = {'a': 'some value', 'b': [1, 2, 3, 4], 7: 'an integer'}
print('b' in d1)
print('\n')
# You can delete values either using the del keyword or the pop method (
d1[5] = 'some value'
print(d1)
del d1[5]
print(d1)
d1['dummy'] = 'another value'
print(d1)
ret = d1.pop('dummy')
print(ret)
print(d1)
print('\n')
# The keys and values method give you iterators of the dict’s keys and values, respectively. The order of the keys depends on the order of their insertion, and these functions output the keys and values in the same respective order:
print(d1.keys())
print(d1.values())
# Since a dict is essentially a collection of 2-tuples, the dict function accepts a list of 2-tuples:
# 一个dict的实质是 两个tuple


words = ['apple', 'bat', 'bar', 'atom', 'book']
by_letter = {}
for word in words:
    letter = word[0]
    print(letter)
    if letter not in by_letter:
        by_letter[letter] = [word]
    else:
        by_letter[letter].append(word)
print(by_letter)

print('\n')
print([1,2,3])
