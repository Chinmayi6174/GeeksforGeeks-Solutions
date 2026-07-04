class Solution:
    def findMin(self, arr):
        # code here
        n=len(arr)
        ans=float("inf")
        low=0
        high=n-1
        while(low<=high):
            mid=(low+high)//2
            if(arr[low]<=arr[mid]):
                if(arr[low]<ans):
                    ans=arr[low]
                low=mid+1
            if(arr[mid]<=arr[high]):
                if(arr[mid]<ans):
                    ans=arr[mid]
                high=mid-1
        return ans
