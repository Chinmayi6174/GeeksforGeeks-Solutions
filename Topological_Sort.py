#in TS no if conditions, no return stmts (except in last)
'''class Solution:
    def topoSort(self, V, edges):
        # Code here
        adj=[[] for i in range(V)]
        ind= [0]*V
        for u,v in edges:
            adj[u].append(v)
            ind[v]+=1
        q=[]
        for i in range(V):
            if ind[i]==0:
                q.append(i)
        res=[]
        while q:
            node= q.pop(0)
            res.append(node)
            for nei in adj[node]:
                ind[nei]-=1
                if ind[nei]==0:
                    q.append(nei)
        return res'''

#same problem using dfs
'''class Solution:
    def topsort(self,V,edges):
        adj=[[] for i in range(V)]
        for u,v in edges:
            adj[u].append(v)
            vis= [False]*V
            st=[]
            def dfs(node):
                vis[node]=True
                for nei in adj[node]:
                    if not vis[nei]:
                        dfs(nei)
                st.append(node)
            for i in range(V):
                if not vis[i]:
                    dfs(i)
            return st[::-1]'''
            
class Solution:
    def topoSort(self, V, edges):
        adj = [[] for _ in range(V)]
        ind = [0] * V
        for u, v in edges:
            adj[u].append(v)
            ind[v] += 1
        q = deque()
        for i in range(V):
            if ind[i] == 0:
                q.append(i)
        res = []
        while q:
            node = q.popleft()
            res.append(node)
            for nei in adj[node]:
                ind[nei] -= 1
                if ind[nei] == 0:
                    q.append(nei)
        # True if cycle exists
        return len(res) != V  
