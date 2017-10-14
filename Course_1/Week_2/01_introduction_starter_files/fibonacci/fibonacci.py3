# Uses python3
def calc_fib(n):
    if n <= 1:
        return n
    prev = 0
    curr = 1

    for i in range(n - 1):
        tmp = curr
        curr = curr + prev
        prev = tmp

    return curr

n = int(input())
print(calc_fib(n))
