class Solution:
    def rotate(self, arr: list[int]) -> None:
        # code here
        arr.insert(0,arr[-1])
        arr.pop()
        return arr 
