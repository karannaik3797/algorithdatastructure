# Uses python3
import sys

def optimal_weight(W, w):
    res = [[0 for x in range(W+1)]for y in range(len(w)+1)]
    
    for i in range(1,len(w)+1):
        for j in range(1,W+1):
            res[i][j]=res[i-1][j]
            if w[i-1]<=j:
                val = res[i-1][j-w[i-1]] + w[i-1]
                if val > res[i][j]:
                    res[i][j]=val
    return res[len(w)][W]
                

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
