import sys
class TreeNode:
    def __init__(self, val=0, left=None, right=None, parent = None, height = None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
        self.height = height

class AvlTree:
    def __init__(self,root):
        self.root = TreeNode(root)
    
def height(N):
    N.height = 1 + max(height(N.right) if N.right else 0,height(N.left) if N.left else 0)
    return N.height      
    
def find(root,x):
    if root.val == x:
        return root 
    elif x< root.val:
        if root.left != None:
            return find(root.left,x)
        return root 
    elif x.> root.val:
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
    parent=k.parent
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
    return parent
def RotateRight(X):
    p =X.parent
    y=X.left
    b=y.right
    y.parent=p
    y.right=x
    x.parent=y
    x.left = b
    b.parent=x

def RotateLeft(X):
    p =X.parent
    y=X.right
    b=y.left
    y.parent=p
    y.left=x
    x.parent=y
    x.right = b
    b.parent=x

def AvlInsert(root,k):
    Insert(root,k)
    N=find(root,k)
    Rebalance(N)

def AvlDelete(N):
    M = Delete(N)
    Rebalance(M)
    
def Rebalance(N):
    P = N.parent
    if N.left.height>N.right.height+1:
        RebalanceRight(N)
    if N.rigth.height>N.left.height+1:
        RebalanceLeft(N)
    Height(N)
    if P!=None:
        Rebalance(P)

def RebalanceRight(N):
    M = N.left
    if M.right.height > M.left.height:
        RotateLeft(M)
    RotateRight(N)
    Height(N)
    
def RebalanceLeft(N):
    M = N.right
    if M.left.height>M.right.height:
        RotateRight(M)
    RotateLeft(N)
    Height(N)

def MergeWithRoot(R1,R2,T):
    T.left = R1
    T.right = R2
    R1.parent = T
    R2.parent = T
    return T

def MergeRoot(R1,R2):
    T = find(R1,sys.maxsize)
    Delete(T)
    MergeWithRoot(R1,R2,T)

def AvlTreeMerge(R1,R2,T):
    if abs(R1.height- R2.height)<=1:
        MergeWithRoot(R1,R2,T)
        height(T)
        return T
    elif R1.height > R2.height:
        R = AvlTreeMerge(R1.right,R2,T)
        R1.right =R
        R.parent = R1
        Rebalance(R1)
        return root
    elif R1.height < R2.height:
        R = AvlTreeMerge(R1,R2.left,T)
        R2.left = R
        R.parent = R2
        Rebalance(R1)
        return root
