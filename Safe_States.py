class Solution:
    def safeNodes(self, V, edges):
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
        vis = [0] * V
        path = [0] * V
        safe = [0] * V
        def dfs(node):
            vis[node] = 1
            path[node] = 1
            for nei in adj[node]:
                if not vis[nei]:
                    if dfs(nei):
                        return True
                elif path[nei]:
                    return True
            path[node] = 0
            safe[node] = 1
            return False
        for i in range(V):
            if not vis[i]:
                dfs(i)
        return [i for i in range(V) if safe[i]]
