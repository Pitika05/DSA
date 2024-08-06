#User function Template for python3

class Solution:
    def armstrongNumber (self, n):
        # code here 
        temp=n
        sum=0
        while n>0:
            digit=n%10
            sum+=digit*digit*digit
            n//=10
        if temp==sum:
            return "true"
        else:
            return "false"
            
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = input()
        n = int(n)
        ob = Solution()
        print(ob.armstrongNumber(n))

# } Driver Code Ends