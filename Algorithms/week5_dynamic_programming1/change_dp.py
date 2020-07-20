# Uses python3
import sys

def get_change(m):
    L = {}
    coins = [1,4,3]
    n = len(coins)
    table = []
    for x in range(m+1):
        table.append(sys.maxsize)
   
    table[0] = 0
    for i in range(1,m+1):
        for j in range(n):
            if coins[j]<=i:
                subres = table[i-coins[j]]
                if(subres!= sys.maxsize and subres+1<table[i]):
                    table[i] = subres+1
    return table[m]


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
