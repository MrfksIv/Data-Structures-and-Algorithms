# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n
    prev = 0
    curr = 1

    for i in range(n - 1):
        tmp = curr
        curr = (curr + prev) % 10
        prev = tmp

    return curr

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))
