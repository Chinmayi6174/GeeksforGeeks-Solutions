class Solution:
    def isCyclic(self, V, edges):
        #code here
        #using Kahn's Algorithm (BFS Topological Sort) to detect a cycle
        adj = [[] for _ in range(V)]
        indegree = [0] * V
        # Build graph
        for u, v in edges:
            adj[u].append(v)      # FIX: append v, not V
            indegree[v] += 1
        q = deque()
        # Push all nodes with indegree 0
        for i in range(V):
            if indegree[i] == 0:
                q.append(i)
        count = 0
        while q:
            node = q.popleft()
            count += 1
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        # If all vertices were processed, no cycle exists
        return count != V
