#User function Template for python3

class Solution:
	def maximumMatch(self, G):
		#code here
        n = len(G)      # Number of applicants
        m = len(G[0])   # Number of jobs

        FREE = -1
        match = [FREE] * m
        
        def canMatch(applicant, visited):
            for job in range(m):
                if G[applicant][job] == 1 and not visited[job]:
                    visited[job] = True
                    if match[job] == FREE or canMatch(match[job], visited):
                        match[job] = applicant
                        return True
            return False

        matches = 0
        for applicant in range(n):
            visited = [False] * m
            if canMatch(applicant, visited):
                matches += 1

        return matches

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		m, n = map(int, input().strip().split())
		G = []
		for i in range(m):
			G.append(list(map(int, input().strip().split())))
		obj = Solution()
		ans = obj.maximumMatch(G)
		print(ans)
# } Driver Code Ends