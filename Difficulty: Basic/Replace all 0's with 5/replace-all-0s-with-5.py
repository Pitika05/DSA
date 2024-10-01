#function should return an integer
#your task is to compplete this function
class Solution:
    def convertFive(self,n):
        #Code here
        n_str = str(n)
        replace_str = n_str.replace('0','5')
        return int(replace_str)


#{ 
 # Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n=int(input())
        print(Solution().convertFive(n))
# Contributed by: Harshit sidhwa

# } Driver Code Ends