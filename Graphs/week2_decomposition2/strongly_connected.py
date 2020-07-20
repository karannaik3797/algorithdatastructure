#Uses python3

import sys

sys.setrecursionlimit(200000)


def dfs(adj, x, visited, stack):
    visited[x] = 1
    for i in range(len(adj[x])):
        if not visited[adj[x][i]]:
            visited[adj[x][i]] = 1
            dfs(adj, adj[x][i], visited, stack)
    stack.append(x)

def reverseEdges(adj):
    r_adj = [[] for _ in range(len(adj))]
    for i in range(len(adj)):
        for j in range(len(adj[i])):
            r_adj[adj[i][j]].append(i)
    return r_adj

def number_of_strongly_connected_components(adj):
    result = 0
    stack = []
    visited = [0] * len(adj)
    for i in range(len(adj)):
        if not visited[i]:
            dfs(adj, i, visited, stack)
    r_adj = reverseEdges(adj)
    visited = [0] * len(adj)
    while stack:
        x = stack.pop()
        if not visited[x]:
            dfs(r_adj, x, visited, [])
            result+=1
    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(number_of_strongly_connected_components(adj))
