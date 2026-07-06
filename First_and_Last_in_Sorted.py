class Solution:
    def find(self, arr, x):
        
        first = -1
        last = -1
        
        # Find first occurrence
        low, high = 0, len(arr) - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            if arr[mid] == x:
                first = mid
                high = mid - 1   # search on left side
            elif arr[mid] < x:
                low = mid + 1
            else:
                high = mid - 1
        
        # Find last occurrence
        low, high = 0, len(arr) - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            if arr[mid] == x:
                last = mid
                low = mid + 1    # search on right side
            elif arr[mid] < x:
                low = mid + 1
            else:
                high = mid - 1
        
        return [first, last]
