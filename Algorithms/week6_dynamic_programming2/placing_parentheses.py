import sys

def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def get_maximum_value(dataset):
    for i in range(len(digits)):
        nmax[i][i] = digits[i]
        nmin[i][i] = digits[i]

    for s in range(0, len(digits)):
        for i in range(0, len(digits) - s - 1):
            j = i + s + 1
            min_value, max_value = min_max_value(i, j)
            nmax[i][j] = max_value
            nmin[i][j] = min_value

def min_max_value(i, j):
    min_value = sys.maxsize
    max_value = -sys.maxsize
    for k in range(i, j):
        a = evalt(nmax[i][k], nmax[k+1][j], ops[k])
        b = evalt(nmax[i][k], nmin[k+1][j], ops[k])
        c = evalt(nmin[i][k], nmax[k+1][j], ops[k])
        d = evalt(nmin[i][k], nmin[k+1][j], ops[k])
        min_value = min(min_value, a, b, c, d)
        max_value = max(max_value, a, b, c, d)
    return min_value, max_value

 

if __name__ == "__main__":
    dataset = input()
    digits = list(map(int, dataset[0::2]))
    ops = list(dataset[1::2])
    nmin = [[0 for x in range(len(digits))] for y in range(len(digits))]
    nmax = [[0 for x in range(len(digits))] for y in range(len(digits))]
    get_maximum_value(dataset)
    print(nmax[0][len(digits) - 1])
