# python3
import random
import sys
from collections import namedtuple

class LCS:
    def __init__(self):
        self.res = [0]
    def hash_func(self,s,p,x):
        ans = 0
        for c in reversed(s):
            ans = (((ans*x+ord(c))%p + p)%p)
        return ans
    def computehashes(self,S,P,p,x):
        s=len(S)
        pn = P
        rest = [None]*(s-pn+1)
        M = S[s-pn:s]
        rest[s-pn]=self.hash_func(M,p,x)
        for i in range(s-pn-1,-1,-1):
            rest[i]=(rest[i+1]*x + ord(S[i])- pow(x,pn,p)*ord(S[i+pn]))%p
        return rest
    def post(self,s,t,mid):
        _prime = 1000000009
        x = random.randint(0,_prime)
        string1 = self.computehashes(s,mid,_prime,x)
        string2 = self.computehashes(t,mid,_prime,x)
        for i in range(len(string2)):
            for j in range(len(string1)):
                if string2[i] == string1[j]:
                    self.res[0] = (i,j)
                    return True
                else:
                    return False
                
    def solve(self,s,t):
        sl = len(s)
        tl =len(t)
        low = 0
        resl = self.res[0]
        high = min(sl,tl)
        while (low<high):
            mid = low + (high - low)//2
            if self.post(s,t,mid):
                low = mid+1
            else:
                right = mid 
        return resl[0],resl[1],low-1
    
for line in sys.stdin.readlines():
    s, t = line.split()
    lcs = LCS()
    ans1,ans2,ans3 = lcs.solve(s, t)
    print(ans1, ans2, ans3)
