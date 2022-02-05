# https: // www.enjoyalgorithms.com/blog/find-the-majority-element-in-an-array
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


arr = [6, 13, 13, 2, 13]
print(getMajorityElement(arr, len(arr)))
arr2 = [1, 2, 4, 5, 7, 8, 8, 8, 8, 8, 8, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]
print(getMajorityElement(arr2, len(arr2)))
arr3 = [1, 2, 4, 5, 7, 8, 8, 8, 8, 8, 8, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]

pi = (len(arr3))//2
print(pi)
print(arr3[:pi])
print(arr3[pi:])
