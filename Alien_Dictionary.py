from collections import deque
class Solution:
    def findOrder(self, words):
        adj = {}
        ind = {}
        # Initialize graph
        for word in words:
            for ch in word:
                if ch not in adj:
                    adj[ch] = []
                if ch not in ind:
                    ind[ch] = 0
        # Build graph
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]
            ml = min(len(w1), len(w2))
            # Invalid case
            if len(w1) > len(w2) and w1[:ml] == w2[:ml]:
                return ""
            for j in range(ml):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].append(w2[j])
                        ind[w2[j]] += 1
                    break
        # Topological Sort
        q = deque()
        for ch in ind:
            if ind[ch] == 0:
                q.append(ch)
        res = []
        while q:
            node = q.popleft()
            res.append(node)
            for nei in adj[node]:
                ind[nei] -= 1
                if ind[nei] == 0:
                    q.append(nei)
        # Cycle detection
        if len(res) != len(ind):
            return ""
        return "".join(res) #join will convert the list into str
