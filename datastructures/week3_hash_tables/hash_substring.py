# python3
import random
def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def hash_func(s,p,x):
    ans = 0
    for c in reversed(s):
        ans = (((ans*x+ord(c))%p + p)%p)
    return ans

def computehashes(S,P,p,x):
    s=len(S)
    pn = len(P)
    res = [None]*(s-pn+1)
    M = S[s-pn:s]
    res[s-pn]=hash_func(M,p,x)
    y = 1
    for i in range (1,pn+1):
        y= (y*x)%p
    for i in range(s-pn-1,-1,-1):
        res[i]=(res[i+1]*x + ord(S[i])- y*ord(S[i+pn]))%p
    return res

def get_occurrences(pattern, text): 
    _prime = 100000007
    x = random.randint(0,_prime)
    phash = hash_func(pattern,_prime,x)
    res=[]
    hashes = computehashes(text,pattern,_prime,x)
    for i in range(0,len(text)-len(pattern)+1):
        if hashes[i] != phash :
            continue
        if text[i:i+len(pattern)]==pattern:
            res.append(i)
    return res

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

