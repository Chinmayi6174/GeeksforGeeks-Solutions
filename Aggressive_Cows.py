class Solution:
    def aggressiveCows(self, stalls, k):
        stalls.sort()
        def ican(dist):
            last=stalls[0]
            c=1
            for i in range(1,len(stalls)):
                if stalls[i]-last>=dist:
                    c+=1
                    last=stalls[i]
                    if c>=k:
                        return True
            return False
        l=0
        r= stalls[-1] - stalls[0] #or stalls[n-1] - stalls[0]
        ans=0
        while l<=r:
            mid=(l+r)//2
            if ican(mid):
                ans=mid
                l=mid+1
            else:
                r=mid-1
        return ans
