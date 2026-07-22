from collections import deque

class Solution:
    def isCycle(self, V, edges):
        # Build adjacency list
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = [False] * V

        def bfs(start):
            q = deque()
            q.append((start, -1))  # (node, parent)
            visited[start] = True

            while q:
                node, parent = q.popleft()
                for nei in adj[node]:
                    if not visited[nei]:
                        visited[nei] = True
                        q.append((nei, node))
                    elif nei != parent:
                        return True
            return False

        # Check all components
        for i in range(V):
            if not visited[i]:
                if bfs(i):
                    return True

        return False
