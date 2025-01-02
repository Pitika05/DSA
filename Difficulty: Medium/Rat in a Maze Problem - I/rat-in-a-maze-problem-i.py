#User function Template for python3
class Solution:
    # Function to find all possible paths
    def findPath(self, mat):
        # code here
        n=len(mat)
        
        if mat[0][0]==0 or mat[n-1][n-1]==0:   #if the starting or ending cell is blocked
            return []
            
        visited=[[False]* n for _ in range(n)]
        result=[]
        di = [1, 0, 0, -1]  
        dj = [0, -1, 1, 0]  
        directions = ['D', 'L', 'R', 'U']
        
        def dfs(sr,sc,path):
            def is_valid(x, y):
                return 0 <= x < n and 0 <= y < n and mat[x][y] == 1 and not visited[x][y]

            if sr==n-1 and sc==n-1:     #if destination is reached.
                result.append(path)
                return 
            
            visited[sr][sc]=True
            
            for i in range(4):  
                new_sr, new_sc = sr + di[i], sc + dj[i]
                if is_valid(new_sr, new_sc):  
                    dfs(new_sr, new_sc, path + directions[i])

            visited[sr][sc] = False  
        
        dfs(0,0,'')
        
        return sorted(result)

            
            
            
        
            
            





#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input().strip())

    for _ in range(t):
        input_line = input().strip()
        mat = eval(input_line)

        solution = Solution()
        result = solution.findPath(mat)

        if not result:
            print("[]")
        else:
            print(" ".join(result))
        print("~")

# } Driver Code Ends