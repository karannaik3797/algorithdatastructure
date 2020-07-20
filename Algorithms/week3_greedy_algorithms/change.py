# Uses python3
import sys

def get_change(m):
    n = 0
    if m >= 10:
        n = m//10
        m = m%10
    if 5 <= m < 10:
        n += (1+m%5)
        
    if m < 5:
        n += m
    return n

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
