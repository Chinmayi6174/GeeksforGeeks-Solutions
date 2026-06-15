class Solution:
    def ratInMaze(self, maze):
        # code here
        n = len(maze)
        res = []
        path=[]
        def bt(r,c):
            if r==n-1 and c==n-1:
                res.append("".join(path))
                return
            #down
            maze[r][c] = 0
            if r+1<n and maze[r+1][c]==1:
                path.append("D")
                bt(r+1,c)
                path.pop()
            #left
            if c-1>-1 and maze[r][c-1]==1:
                path.append("L")
                bt(r,c-1)
                path.pop()
            #right
            if c+1<n and maze[r][c+1]==1:
                path.append("R")
                bt(r,c+1)
                path.pop()
            #up
            if r-1>-1 and maze[r-1][c]==1:
                path.append("U")
                bt(r-1,c)
                path.pop()
            maze[r][c]=1
        if maze[0][0]==1:
            bt(0,0)
        return res
