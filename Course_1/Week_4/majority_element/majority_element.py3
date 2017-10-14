# Uses python3
import sys

def get_majority_element(a, left, right):
    cnt_dict = {}
    for elem in a:
        try:
            cnt_dict[elem] += 1
        except:
            cnt_dict[elem] = 1
    
    max_cnt = -1
    for key in cnt_dict.keys():
        if cnt_dict[key] > len(a)/2:
            max_cnt = cnt_dict[key]
    
    return max_cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
