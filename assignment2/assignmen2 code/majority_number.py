# Suppose we have a list of n numbers. The list is guaranteed to have a number
# which appears more than n/2 times on it. Devise a good algorithm to find the
# Majority element
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


arr = [1, 2, 4, 5, 7, 8, 8, 8, 8, 8, 8, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]
print(' the majority number in the array is ', majority_number(arr))
