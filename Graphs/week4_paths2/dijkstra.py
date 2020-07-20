#Uses python3

import sys
 
class MinHeap:
    def __init__(self, num_workers):
        self._data = []
        self.n = num_workers
        for i in range(num_workers):
            self._data.append((i, float('inf')))

    def ChangePriority(self, index, priority):
        res = 0
        for i in range(len(self._data)):
            if self._data[i][0] == index:
                res = i
                break
        old_p = self._data[res][1]
        self._data[res] = (self._data[res][0], priority)
        if priority < old_p:
            self.SiftUp(res)
        else:
            self.SiftDown(res)

    def RepairHeap(self):
        for i in range(int(self.n / 2), -1, -1):
            self.SiftDown(i)

    def Parent(self, i):
        return int((i-1)/2)

    def LeftChild(self, i):
        return 2 * i + 1

    def RightChild(self, i):
        return 2 * i + 2
    
    def get(self):
        res =  self._data.pop(0)
        self.SiftDown(0)
        return res

    def CompareWorker(self, node1, node2):
        if node1[1] != node2[1]:
            return node1[1] < node2[1]
        else:
            return node1[0] < node2[0]

    def SiftUp(self, i):
        while i > 0 and self.CompareWorker(self._data[i], self._data[self.Parent(i)]):
            self._data[i], self._data[self.Parent(i)] = self._data[self.Parent(i)], self._data[i]
            i = self.Parent(i)


    def SiftDown(self, i):
        minIndex = i
        left = self.LeftChild(i)
        if left < len(self._data) and self.CompareWorker(self._data[left], self._data[minIndex]):
            minIndex = left

        right = self.RightChild(i)
        if right < len(self._data) and self.CompareWorker(self._data[right], self._data[minIndex]):
            minIndex = right
        if i != minIndex:
            self._data[i], self._data[minIndex] = self._data[minIndex], self._data[i]
            self.SiftDown(minIndex)
   
    def empty(self):
         if self._data != []:
            return False
         else:
            return True

def distance(adj, cost, s, t):
    #write your code here
    dist=[float('inf')]*len(adj)
    dist[s] = 0
    pq = MinHeap(len(adj))
    pq.ChangePriority(s, dist[s])
    while not pq.empty():
         u = pq.get()
         u_index = u[0]
         for v in adj[u_index]:
             v_index = adj[u_index].index(v)
             if dist[v] > dist[u_index] + cost[u_index][v_index]:
                dist[v] = dist[u_index] + cost[u_index][v_index]
                pq.ChangePriority(v, dist[v])
    if dist[t] == float('inf'):
        return -1
    return dist[t]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
