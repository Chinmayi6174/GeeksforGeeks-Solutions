#User function Template for python3
class Solution:
    def findCeil(self, arr, x):
        # code here
        low = 0
        high = len(arr) - 1
        ans = -1

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] >= x:
                ans = mid
                high = mid - 1   # search for first occurrence
            else:
                low = mid + 1

        return ans
