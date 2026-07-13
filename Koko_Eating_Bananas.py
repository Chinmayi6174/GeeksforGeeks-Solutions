class Solution:
    def kokoEat(self, arr, k):
        low = 1
        high = max(arr)

        while low <= high:
            mid = (low + high) // 2

            hours = 0

            for num in arr:
                hours += (num + mid - 1) // mid

            if hours <= k:
                high = mid - 1
            else:
                low = mid + 1

        return low
        
        
        '''from math import ceil
arr=[1,3,5,9]
k=6
low=1
high=max(arr)
while(low<=high):
    mid=(low+high)//2
    sum=0
    for num in arr:
        sum+=ceil(num/mid)
    if(sum<=k):
        high=mid-1
    else:
        low=mid+1
print(low)'''
