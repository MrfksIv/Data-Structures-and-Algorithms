# Uses python3
import sys

def optimal_weight_old(W, w):
    # write your code here
    result = 0
    for x in w:
        if result + x <= W:
            result = result + x
    return result


def optimal_weight(cap_W, w):
    max_weights = [[0] * (cap_W + 1) for i in range(len(w) + 1)]
   
    for i, weight in enumerate(w):
        i += 1
        for capacity in range(cap_W + 1):
            # Handle the case where the weight of the current item is greater
            # than the "running capacity" - we can't add it to the knapsack
            if weight > capacity:
                max_weights[i][capacity] = max_weights[i - 1][capacity]
            else:
                candidate1 = max_weights[i - 1][capacity]
                candidate2 = max_weights[i - 1][capacity - w[i-1]] + weight

                max_weights[i][capacity] = max(candidate1, candidate2)
    return max_weights[len(w)][cap_W]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))