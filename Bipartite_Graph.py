from collections import deque

class Solution:
    def isBipartite(self, V, edges):
        
        # Build adjacency list
        adj = [[] for _ in range(V)]
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        # -1 means uncolored
        color = [-1] * V
        
        def bfs(start):
            q = deque([start])
            color[start] = 0
            
            while q:
                node = q.popleft()
                
                for nei in adj[node]:
                    
                    # If uncolored, assign opposite color
                    if color[nei] == -1:
                        color[nei] = 1 - color[node]
                        q.append(nei)
                    
                    # Same color on adjacent nodes
                    elif color[nei] == color[node]:
                        return False
            
            return True
        
        # Handle disconnected components
        for i in range(V):
            if color[i] == -1:
                if not bfs(i):
                    return False
        
        return True
        
        
        
#another way using dfs
'''def isBiparite(self,V,edges):
    adj = [[] for _ in range(V)]
    for u,v in edges:
        adj[u].append(v)
        adj[v].append(u)
    color = [-1]*v
    for i in range(V):
        if color[i]==-1:
            if not self.dfs(i,0,adj,color):
                return False
    def dfs(self, node, col, adj, color):
        color[node]=col
        for neighbor in adj[node]:
            if color[neighbor]==-1:
                if not in self.dfs(neighbor,1-col,adj,color):
                    return False
            elif color[neighbor]==col:
                return False
        return True'''
