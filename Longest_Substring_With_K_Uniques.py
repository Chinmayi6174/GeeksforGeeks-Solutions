class Solution:
    def longestKSubstr(self, s, k):
        # code here
        l=0
        max_len=-1
        freq={}
        n=len(s)
        for r in range(n):
            if s[r] in freq:
                freq[s[r]]+=1
            else:
                freq[s[r]]=1
            while len(freq)>k:
                freq[s[l]]-=1
                if freq[s[l]]==0:
                    del freq[s[l]]
                l+=1
            if len(freq)==k:
                ws=(r-l)+1
                max_len= max(max_len, ws)
        return max_len
