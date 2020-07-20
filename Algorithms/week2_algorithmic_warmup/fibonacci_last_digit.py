# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    res = []
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        res.append(0)
        res.append(1)
        for i in range(2,n+1):
            res.append((res[i-1]+res[i-2])%10)
        return res[n]

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))
