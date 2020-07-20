# python3
#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**9) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

def IsBinarySearchTree(tree):
    prev = None
    cur = 0
    stack = []
    
    while True:
        if cur != -1:
            stack.append(cur)
            cur = tree[cur][1]
        elif stack:
            cur = stack.pop()
            if prev != None and tree[cur][0] < tree[prev][0]:
                return False                
            prev = cur
            cur = tree[cur][2]
        else:
            break
    return True

def main():
    nodes = int(sys.stdin.readline().strip())
    if nodes == 0:
        print("CORRECT")
    else:
        tree = []       
        for i in range(nodes):
            tree.append(list(map(int, sys.stdin.readline().strip().split())))
        if IsBinarySearchTree(tree):
            print("CORRECT")
        else:
            print("INCORRECT")

threading.Thread(target=main).start()
