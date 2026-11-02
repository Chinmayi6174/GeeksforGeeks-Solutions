class Solution:
    def findElements(self,arr):
        # code here
        arr.remove(max(arr))
        arr.remove(max(arr))
        arr.sort()
        return arr
