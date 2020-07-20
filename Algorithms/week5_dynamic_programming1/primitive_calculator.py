# Uses python3
import sys

def optimal_sequence(n):
    if n==1:
        return [1]
    ops = min_ops(n)
    return ops_list(n,ops)
def ops_list(n,ops):
    sequence = []
    while n>0 :
        sequence.append(n)
        if n%2 != 0 and n%3 != 0:
             n = n-1
        elif n%2 == 0 and n%3 == 0:
            n = n//3
        elif n%2 == 0 :
            if ops[n-1] < ops[n//2]:
                n = n-1
            else:
                n = n//2
        elif n%3 == 0 :
            if ops[n-1] < ops[n//3]:
                n = n-1
            else:
                n = n//3
    return list(reversed(sequence))
    
def min_ops(n):
    result = []
    for i in range(n+1):
        result.append(0)
    for i in range(2,n+1):
        min1 = result[i-1]
        min2 = sys.maxsize
        min3 = sys.maxsize
        if i%2 == 0:
            min2 = result[int(i/2)]
        if i%3 == 0:
            min2 = result[int(i/3)]
        minop=min(min1,min2,min3)
        result[i]=minop+1
    return result
            
            
            
            
input = sys.stdin.read()
n = int(input)
sequence = (optimal_sequence(n))
print(len(list(sequence)) - 1)
for x in list(sequence):
    print(x, end=' ')
