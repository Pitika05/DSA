#User function Template for python3

class Solution:

    def findMinDiff(self, A,N,M):
        # code here
        A.sort()
        
        if N==0 or M==0:
            return 0
        
        if N<M:
            return -1
        
        min_diff=float('inf')
        for i in range(N-M+1):
            diff=A[i+M-1]-A[i]
            if diff<min_diff:
                min_diff=diff
        return min_diff


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        N = int(input())
        A = [int(x) for x in input().split()]
        M = int(input())


        solObj = Solution()

        print(solObj.findMinDiff(A,N,M))
# } Driver Code Ends