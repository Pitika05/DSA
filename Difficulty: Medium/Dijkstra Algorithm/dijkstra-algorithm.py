import heapq

class Edge:
    def __init__(self, to, cost):
        self.to = to
        self.cost = cost

class Graph:
    def __init__(self, n):
        self.n = n
        self.edge_count = 0
        self.graph = [[] for _ in range(n)]

    def add_edge(self, from_node, to_node, cost):
        self.edge_count += 1
        self.graph[from_node].append(Edge(to_node, cost))

class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        #code here
        graph = Graph(V)
        for u in range(V):
            for v, w in adj[u]:
                graph.add_edge(u, v, w)
        
        # Initialize distance array and priority queue
        dist = [float('inf')] * V
        dist[S] = 0
        priority_queue = [(0, S)]  # (cost, node)
        
        visited = [False] * V
        prev = [None] * V
        
        while priority_queue:
            current_dist, current_node = heapq.heappop(priority_queue)
            
            if visited[current_node]:
                continue
            
            visited[current_node] = True
            
            for edge in graph.graph[current_node]:
                if visited[edge.to]:
                    continue
                
                new_dist = current_dist + edge.cost
                if new_dist < dist[edge.to]:
                    dist[edge.to] = new_dist
                    prev[edge.to] = current_node
                    heapq.heappush(priority_queue, (new_dist, edge.to))
        
        return dist


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        S=int(input())
        ob = Solution()
        
        res = ob.dijkstra(V,adj,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends