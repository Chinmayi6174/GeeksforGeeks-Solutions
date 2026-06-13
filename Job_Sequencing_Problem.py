class Solution:
    def jobSequencing(self, deadline, profit):
        n = len(deadline)
        jobs = list(zip(deadline, profit))
        jobs.sort(key=lambda x: x[1], reverse=True)
        max_deadline = max(deadline)
        parent = list(range(max_deadline + 1))
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        count = 0
        total_profit = 0
        for d, p in jobs:
            available = find(d)
            if available > 0:
                count += 1
                total_profit += p
                parent[available] = find(available - 1)
        return [count, total_profit]
