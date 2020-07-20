# python3
#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**9) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

def IsBinarySearchTree(tree):
    stack = [0]
    cur = 0
    
    while True:
        if tree[cur][1] != -1:
            stack.append(tree[cur][1])
            if tree[cur][0] <= tree[tree[cur][1]][0]:
                return False
        if tree[cur][2] != -1:
            stack.append(tree[cur][2])
            if tree[cur][0] > tree[tree[cur][2]][0]:    
                return False
        if stack != []:
            cur = stack.pop(0)
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
