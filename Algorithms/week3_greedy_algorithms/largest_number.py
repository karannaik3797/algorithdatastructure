#Uses python3

import sys
import functools
def cmp(a,b):
    s1=str(a)
    s2=str(b)
    num1=int(s1+s2)
    num2=int(s2+s1)
    if(num1<num2):
        return 1
    else:
        return -1
        

def largest_number(a):
    a=sorted(a,key=functools.cmp_to_key(cmp))
    res =""
    for c in a:
        res+=str(c)
    return int(res)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
