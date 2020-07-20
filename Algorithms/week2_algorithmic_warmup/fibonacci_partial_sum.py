# Uses python3
import sys
def get_pisano_period(m):
    a = 0
    b = 1
    c = a+b
    for i in range(m*m):
8        c = (a+b)%m
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

def fibonacci_partial_sum_naive(from_, to):
    return( (get_fibonacci_huge_naive(to+2, 10) + 10 - get_fibonacci_huge_naive(from_+1, 10)) % 10) 

if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))
