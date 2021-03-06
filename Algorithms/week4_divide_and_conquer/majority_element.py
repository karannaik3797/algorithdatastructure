# Uses python3
import sys

def get_majority_element(a, left, right):
    l =left 
    r =right-1
    a.sort()
    count = 1
    if left == right:
        return -1
    if left+1 == right:
        return 1
    for i in range(len(a)-1):
        if a[i]==a[i+1]:
            count += 1
            if (count > right/2):
                return 1
        else:
            count = 1
    return -1
   
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
