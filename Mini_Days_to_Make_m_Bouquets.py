class Solution:
    def minDaysBloom(self, arr, k, m):
        # Code here
        if(k*m>len(arr)):
            return -1
        low= min(arr)
        high= max(arr)
        while(low<=high):
            mid= (low+high)//2
            no_of_flowers=0
            no_of_bou= 0
            for num in arr:
                if (num<=mid):
                    no_of_flowers+=1
                    if(no_of_flowers==k):
                        no_of_bou+=1
                        no_of_flowers=0
                else:
                    no_of_flowers=0
            if(no_of_bou>=m):
                high=mid-1
            else:
                low= mid+1
        return low
        
