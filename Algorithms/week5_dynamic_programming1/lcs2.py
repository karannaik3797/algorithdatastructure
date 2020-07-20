#Uses python3

import sys

def lcs2(a, b):
    res = [[0 for i in range(len(b)+1)]for j in range(len(a)+1)]
    for x in range(1,len(b)+1):
        for y in range(1,len(a)+1):
            if a[y-1]==b[x-1]:
                res[y][x]=res[y-1][x-1]+1
            else:
                res[y][x]=max(res[y-1][x],res[y][x-1])
    return res[len(a)][len(b)]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
0
