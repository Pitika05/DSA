#User function template for Python

class Solution:
    def binarysearch(self, arr, k):
        # Code Here
        low=0
        high=len(arr)-1
        
        while low <= high:
            mid = (low+high) // 2
            #if mid == target value then return the mid
            if arr[mid]==k:
                return mid
            #if mid is less then target value then increment low
            elif arr[mid]<k:
                low = mid+1
            #if mid is greater than target value then decrement high
            else:
                high = mid-1
        return -1
        
        
        



#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        k = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.binarysearch(arr, k)
        print(res)

# } Driver Code Ends