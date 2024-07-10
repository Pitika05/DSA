class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        # Code here
        def dfs(i, at, visited, ordering):
            visited[at] = True
            edges = adj[at]
            for edge in edges:
                if not visited[edge]:
                    i = dfs(i, edge, visited, ordering)
            ordering[i] = at
            return i - 1

        # N is the number of nodes (V)
        N = V
        visited = [False] * N
        ordering = [0] * N
        i = N - 1

        for at in range(N):
            if not visited[at]:
                i = dfs(i, at, visited, ordering)

        return ordering




#{ 
 # Driver Code Starts
# Driver Program

import sys
sys.setrecursionlimit(10**6)
        
def check(graph, N, res):
    if N!=len(res):
        return False
    map=[0]*N
    for i in range(N):
        map[res[i]]=i
    for i in range(N):
        for v in graph[i]:
            if map[i] > map[v]:
                return False
    return True

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        e,N = list(map(int, input().strip().split()))
        adj = [[] for i in range(N)]
        
        for i in range(e):
            u,v=map(int,input().split())
            adj[u].append(v)
            
        ob = Solution()
        
        res = ob.topoSort(N, adj)
        
        if check(adj, N, res):
            print(1)
        else:
            print(0)
# Contributed By: Harshit Sidhwa

# } Driver Code Ends