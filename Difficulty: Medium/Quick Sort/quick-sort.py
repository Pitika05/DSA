#User function Template for python3

class Solution:
    #Function to sort a list using quick sort algorithm.
    def quickSort(self,arr,low,high):
        # code here
        if low < high:
            pi = self.partition(arr,low,high)
            
            self.quickSort(arr,low,pi-1)
            self.quickSort(arr,pi+1,high)
    
    def partition(self,arr,low,high):
        # code here
        pivot = arr[high]
        
        # Index of smaller element
        i = low - 1
        
        # Traverse the array and rearrange based on pivot
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                # Swap arr[i] and arr[j]
                arr[i], arr[j] = arr[j], arr[i]
        
        # Swap the pivot element with the element at index i + 1
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        
        # Return the partition index
        return i + 1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().quickSort(arr,0,n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()

# } Driver Code Ends