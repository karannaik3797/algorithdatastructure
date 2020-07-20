# Uses python3
import sys
import math

def mergeSortInversions(arr):
    if len(arr) == 1:
        return arr, 0
    else:
        l = len(arr)
        m = math.floor(l/2)
        a = arr[:m]
        b = arr[m:]
        a, ai = mergeSortInversions(a)
        b, bi = mergeSortInversions(b)
        c = []
        i = 0
        j = 0
        inversions = 0 + ai + bi
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
            inversions += (len(a)-i)
    c += a[i:]
    c += b[j:]
    return c, inversions
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    a, b = mergeSortInversions(a)
    print(b)