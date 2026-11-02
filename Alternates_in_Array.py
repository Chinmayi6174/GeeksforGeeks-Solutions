class Solution:
    def getAlternates(self, arr):
        # Code Here
        new_arr= []
        for i in range(len(arr)) :
            if i%2==0:
                new_arr.append(arr[i])
        return new_arr
