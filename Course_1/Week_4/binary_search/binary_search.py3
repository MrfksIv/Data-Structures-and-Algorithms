# Uses python3
import sys

def binary_search(a=None, low=0, high=None, x=None):
    left, right = low, len(a) if high is None else high
    # print(a[low:high], left, right)
    if left >= right-1 and a[left] != x:
        return -1
    
    mid = left + (right - left) // 2
    if x == a[mid]:
        return mid
    elif x < a[mid]:
        return binary_search(a=a, low=left, high=mid, x=x)
    else:
        return binary_search(a=a, low=mid, x=x)

    # write your code here

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a=a, x=x), end = ' ')
