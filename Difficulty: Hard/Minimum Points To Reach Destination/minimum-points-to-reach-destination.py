#User function Template for python3
class Solution:
	def minPoints(self, m, n, points):
		# code here
		m, n = len(points), len(points[0])
        t = [[float('inf')] * n for i in range(m)]         # Initialize the DP table with infinity
 
        t[m-1][n-1] = max(1 - points[m-1][n-1], 1)
        
        for j in range(n-2, -1, -1):
            t[m-1][j] = max(t[m-1][j+1] - points[m-1][j], 1)
        
        for i in range(m-2, -1, -1):
            t[i][n-1] = max(t[i+1][n-1] - points[i][n-1], 1)
        
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                min_points = min(t[i+1][j], t[i][j+1])
                t[i][j] = max(min_points - points[i][j], 1)
        
        return t[0][0]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		m,n = input().split()
		m,n = int(m),int(n)
		points = []
		for _ in range(m):
			temp = [int(x) for x in input().split()]
			points.append(temp)
		ob = Solution()
		ans = ob.minPoints(m,n,points)
		print(ans)




# } Driver Code Ends