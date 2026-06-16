# User function Template for python3
class Solution:
    def graphColoring(self, v, edges, m):
        # code here
        g=[[] for i in range(v)]
        for u,w in edges:
            g[u].append(w)
            g[w].append(u)
        color=[0]*v
        def issafe(node, col):
            for nei in g[node]:
                if color[nei]==col:
                    return False
            return True
        def bt(node):
            if node==v:
                return True
            for col in range(1,m+1):
                if issafe(node,col):
                    color[node]=col
                    if bt(node+1):
                        return True
                    color[node]=0
            return False
        return bt(0)
