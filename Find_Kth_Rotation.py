class Solution:
    def findKRotation(self, arr):
        # code here
        n=len(arr)
        ans=float("inf")
        low=0
        high=n-1
        index=0
        while(low<=high):
            mid=(low+high)//2
            if(arr[low]<=arr[mid]):
                if(arr[low]<ans):
                    ans=arr[low]
                    index=low
                low=mid+1
            if(arr[mid]<=arr[high]):
                if(arr[mid]<ans):
                    ans=arr[mid]
                    index=mid
                high=mid-1
        return index
        
