# Uses python3
import sys


def gcd(a,b):
    if a % b == 0:
        return b
    return gcd(b, a%b)


def lcm_naive(a, b):
    largest = a if a > b else b
    gcd_ = gcd(a, b)
    return gcd_ * largest if gcd_ > 1 else a * b

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))

