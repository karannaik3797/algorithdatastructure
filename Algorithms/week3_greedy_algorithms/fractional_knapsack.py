# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0
    vpw = []
    index = list(range(len(values)))
    for i in range(len(weights)):
        vpw.append(values[i]/weights[i])
            
    index.sort(key = lambda i : vpw[i], reverse = True)
    for i in index:
        if weights[i]<capacity:
            capacity = capacity - weights[i]
            value += vpw[i]*weights[i]
        else:
            value += vpw[i]*capacity
            break
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
