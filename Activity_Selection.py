class Solution:
    def activitySelection(self, start, finish):
        n = len(start)
        # Pair start and finish times
        act = list(zip(start, finish))
        # Sort by finish time
        act.sort(key=lambda x: x[1])
        count = 1
        last_end = act[0][1]
        for i in range(1, n):
            if act[i][0] > last_end:
                count += 1
                last_end = act[i][1]
        return count
