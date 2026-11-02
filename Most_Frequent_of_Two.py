class Solution:
    def moreFrequent(self, arr, x, y):
        x_count = 0
        y_count = 0
        for i in arr:
            if i == x:
                x_count += 1
            elif i == y:
                y_count += 1
        if x_count > y_count:
            return x
        elif y_count > x_count:
            return y
        else:
            return min(x, y)
