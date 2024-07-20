#User function Template for python3

class Solution:
    
    #Function to return a list of lists of integers denoting the members 
    #of strongly connected components in the given graph.
    def tarjans(self, V, adj):
        # code here
        def dfs(at):
            nonlocal id
            
            stack.append(at)
            onStack[at]=True
            ids[at]=low[at]=id
            id+=1
            
            for to in adj[at]:
                if ids[to] == -1:
                    dfs(to)
                if onStack[to]:
                    low[at]= min(low[at], low[to])
            
            if ids[at]==low[at]:
                scc=[]
                while True:
                    node = stack.pop()
                    onStack[node]=False
                    scc.append(node)
                    if node == at:
                        break
                sccs.append(sorted(scc))
        
        #Initialization
        ids=[-1]*V
        low=[-1]*V
        onStack=[False]*V
        stack=[]
        sccs=[]
        id=0
        
        #Run DFS for each vertex
        for i in range(V):
            if ids[i] == -1:
                dfs(i)
        
        return sorted(sccs)
            
        
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3
from collections import OrderedDict 
import sys 

sys.setrecursionlimit(10**6) 

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
        
        for i in range(V):
            adj[i] = list(OrderedDict.fromkeys(adj[i])) 
            
        ob = Solution()
        
        ptr = ob.tarjans(V, adj)
        
        for i in range(len(ptr)):
            for j in range(len(ptr[i])):
                if j==len(ptr[i])-1:
                    print(ptr[i][j],end="")
                else:
                    print(ptr[i][j],end=" ")
            print(",",end="")
        print()
# } Driver Code Ends