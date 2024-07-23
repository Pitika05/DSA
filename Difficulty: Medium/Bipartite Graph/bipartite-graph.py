from collections import deque
class Solution:
	def isBipartite(self, V, adj):
		#code here
		RED,BLACK=1,0
		colors=[-1]*V
		
		def bfs(start,color):
		    queue=deque([(start,color)])
		    colors[start]=color
		    
		    while queue:
		        node,col=queue.popleft()
		        next_color= BLACK if col==RED else RED
		        
		        for neighbor in adj[node]:
		            if colors[neighbor]==col:
		                return False
		            if colors[neighbor]== -1:
		                colors[neighbor]=next_color
		                queue.append((neighbor, next_color))
		    
		    return True
		    
		for i in range(V):
		    if colors[i]== -1:
    		    if not bfs(i, RED):
    		        return False
		return True
		    

#{ 
 # Driver Code Starts

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().strip().split())
		adj = [[] for i in range(V)]
		for i in range(E):
			u, v = map(int, input().strip().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isBipartite(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends