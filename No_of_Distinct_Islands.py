import sys
from typing import List
sys.setrecursionlimit(10**8)
class Solution:
    def countDistinctIslands(self, grid : List[List[int]]) -> int:
        # code here
        def dfs(i,j,vis,grid, n, m,allIndexes):
            for r,c in [[-1,0], [1,0], [0,-1], [0,1]]:
                     nr= r+i
                     nc= c+j
                     if (nr>=0 and nr<n and nc>=0 and nc<m and grid[nr][nc]== 1 and vis[nr][nc]==0):
                          allIndexes.append((nr,nc))
                          vis[nr][nc] =1
                          dfs(nr,nc,vis,grid, n, m,allIndexes)
        n= len(grid)
        m= len(grid[0])
        vis= []
        for i in range(n):
            lst= [0]*m
            vis.append(lst)
        s= set()
        for i in range(n):
            for j in range(m):
                 allIndexes= []
                 shape= []
                 if (grid[i][j] ==1 and vis[i][j]==0):
                    vis[i][j] =1
                    allIndexes.append((i,j))
                    baseRow= i
                    baseCol= j
                    dfs(i, j, vis, grid, n, m , allIndexes)
                    for row, col in allIndexes:
                         shape.append((row- baseRow, col-baseCol))
                    s.add(tuple(shape)) 
        return len(s)
