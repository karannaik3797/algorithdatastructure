#python3

import sys

sys.setrecursionlimit(10000)

class SuffixTree:
    class Node:
        def __init__(self, label):
            self.label = label
            self.out = {}

    def __init__(self, text):
        self.root = self.Node(None)
        self.root.out[text[0]] = self.Node(text)
        for i in range(1, len(text)):
            current = self.root
            j = i
            while j < len(text):
                if text[j] in current.out:
                    child = current.out[text[j]]
                    label = child.label
                    k = j + 1
                    while k - j < len(label) and text[k] == label[k - j]:
                        k += 1
                    if k - j == len(label):
                        current = child
                        j = k
                    else:
                        cExist, cNew = label[k - j], text[k]
                        mid = self.Node(label[:k - j])
                        mid.out[cNew] = self.Node(text[k:])
                        mid.out[cExist] = child
                        child.label = label[k - j:]
                        current.out[text[j]] = mid
                else:
                    current.out[text[j]] = self.Node(text[j:])


def solve(p, q):
    text = p + '#' + q + '$'
    tree = SuffixTree(text)
    while i in tree.root.out:
        sub = ''
        if i != '#':
            if i in tree.root.out['#'].out:
                                 return i
    
                
                
            
            


p = sys.stdin.readline ().strip ()
q = sys.stdin.readline ().strip ()

ans = solve (p, q)

sys.stdout.write (ans + '\n')
