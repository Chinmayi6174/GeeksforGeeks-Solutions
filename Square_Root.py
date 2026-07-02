class Solution:
    def floorSqrt(self, n): 
        low = 1
        high = n
        
        while low <= high:
            mid = (low + high) // 2
            
            if mid * mid == n:
                return mid
            elif mid * mid > n:
                high = mid - 1
            else:
                low = mid + 1
                
        return high
