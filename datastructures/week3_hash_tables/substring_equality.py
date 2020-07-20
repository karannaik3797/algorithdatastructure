# python3

import sys
import random

class Solver:
    
    def __init__(self, string1):
        self.st = string1
        self.m1 = 1000000009
        self.m2 = 1000000007
        self.x = random.randint(0,self.m1)
        self.hash1 = self.hash_func(self.st,self.m1,self.x)
        self.hash2 = self.hash_func(self.st,self.m2,self.x)
    def hash_func(self,s,p,x):
        s = reversed(s)
        ans = [0 for i in range(len(s)+1)]
        for i in range(1,len(s)+1):
            ans[i] = (ans[i-1]*x+ord(s[i-1]))%p 
        return ans   
    
    def ask(self,a,b,l):
        hash1s = (self.hash1[a+l] - (pow(self.x,l,self.m1)*self.hash1[a]))%self.m1
        hash1s2 =(self.hash1[b+l] - (pow(self.x,l,self.m1)*self.hash1[b]))%self.m1
        hash2s = (self.hash2[a+l] - (pow(self.x,l,self.m2)*self.hash2[a]))%self.m2
        hash2s2 =(self.hash2[b+l] - (pow(self.x,l,self.m2)*self.hash2[b]))%self.m2
        if hash1s == hash1s2 and hash2s == hash2s2:
            return True
        else:
            return False
s = sys.stdin.readline()
q = int(sys.stdin.readline())
solver = Solver(s)
for i in range(q):
	a, b, l = map(int, sys.stdin.readline().split())
	print("Yes" if solver.ask(a, b, l) else "No")
