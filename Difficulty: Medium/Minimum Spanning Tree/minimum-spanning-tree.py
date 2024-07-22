#User function Template for python3
import heapq
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        #code here
        # Using a priority queue to implement Prim's algorithm
        min_heap = [(0, 0)]  # (weight, vertex)
        visited = [False] * V
        mst_weight = 0
        
        while min_heap:
            weight, u = heapq.heappop(min_heap)
            
            if visited[u]:
                continue
            
            # Include this vertex in MST
            mst_weight += weight
            visited[u] = True
            
            # Add all adjacent vertices to the heap
            for v, w in adj[u]:
                if not visited[v]:
                    heapq.heappush(min_heap, (w, v))
        
        return mst_weight
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        ob = Solution()
        
        print(ob.spanningTree(V,adj))
# } Driver Code Ends