# Uses python3
from sys import stdin
def get_pisano_period(m):
    a = 0
    b = 1
    c = a+b
    for i in range(m*m):
        c = (a+b)%m
        a,b = b,c
        if (a==0 and b==1):
            return i+1

def get_fibonacci_huge_naive(n, m):
    remainder = n % get_pisano_period(m)
    res = remainder
    f = 0
    s = 1 
    for i in range(1,remainder):
        res = (f+s)%m
        f = s
        s = res
    
    return res % m

def fibonacci_sum_squares_naive(n):
    return (((get_fibonacci_huge_naive(n,10)+get_fibonacci_huge_naive(n-1,10))*get_fibonacci_huge_naive(n,10))%10)

if __name__ == '__main__':
    n = int(stdin.read())
    print(fibonacci_sum_squares_naive(n))
