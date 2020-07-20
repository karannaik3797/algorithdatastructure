# Uses python3
import sys
def gcd_naive(a, b):
    while(b): 
        a, b = b, a % b 
    return a
def lcm_naive(a, b):
    res = gcd_naive(a,b)
    mul = a*b/res
    return (int(mul))

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))

