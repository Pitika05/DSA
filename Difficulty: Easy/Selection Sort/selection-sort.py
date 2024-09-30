#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here 
        min_idx = i
        
        # Loop through the unsorted part of the array to find the minimum
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Return the index of the minimum element found
        return min_idx   
    
    def selectionSort(self, arr,n):
        #code here
        # Loop through each element in the array
        for i in range(n):
            # Select the minimum element index from the unsorted part
            min_idx = self.select(arr, i)
            
            # Swap the found minimum element with the first unsorted element
            arr[i], arr[min_idx] = arr[min_idx], arr[i]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends