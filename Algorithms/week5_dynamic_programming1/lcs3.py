#Uses python3

import sys

def lcs3(a, b, c):
    res = [[[0 for i in range(len(c)+1)] for j in range(len(b)+1)]for k in range(len(a)+1)] 
    for z in range(1,len(c)+1):
        for x in range(1,len(b)+1):
            for y in range(1,len(a)+1):
                if a[y-1]==b[x-1] and b[x-1]==c[z-1]:
                    res[y][x][z]=res[y-1][x-1][z-1]+1
                else:
                    res[y][x][z]=max(res[y-1][x][z],res[y][x-1][z],res[y][x][z-1])
    return res[len(a)][len(b)][len(c)]




if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
