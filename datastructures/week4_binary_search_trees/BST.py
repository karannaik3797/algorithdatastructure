# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 21:26:48 2020

@author: Dell
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None, parent = None, height = None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
        self.height = height

class BinarySearchTree:
    def __init__(self,root):
        self.root = TreeNode(root) 
    
    
def height(self,N):
    N.height = 1 + max(height(N.right) if N.right else 0,height(N.left) if N.left else 0)
    return N.height      
    
def find(root,x):
    if root.val == x:
        return root 
    elif x < root.val:
        if root.left != None:
            return find(root.left,x)
        return root 
    elif x > root.val:
        if root.right != None:
            return find(root.right,x)
        return root
            
def Next(N):
    if N.right != None:
        return LeftDescendant(N.right)
    else:
        return Ancestor(N)
        
def LeftDescendant(N):
    while N.left != None:
        N = N.left
    return N

def Ancestor(N):
    while N.val > N.parent.val:
        N = N.parent
    return N
    
def Insert(root,N):
    k = find(root,N)
    if N.val < k.val:
        k.left = N
        N.parent = k
    elif N.val > k.val:
        k.right = N
        N.parent = k
            
def Delete(k):
    if k.right == None:
        k.left.parent = k.parent
        if  k.parent.val > k.left.val:
            k.parent.left = k.left
        else:
            k.parent.right = k.left
        k.parent = None
        k.left = None
    else:
        j = Next(k)
        if j.left == None:
            j.right.parent = j.parent
            if j.parent.val > j.right.val:
                j.parent.left = j.right
            else:
                j.parent.right = j.right
            j.parent = k.parent
            if k.parent.val < j.val:
                k.parent.left = j
            else:
                k.parent.right = j
            k.parent = None
            k.right = None

