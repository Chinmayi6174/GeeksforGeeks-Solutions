class Solution:
    def orangesRot(self, mat):
        #code here
        rows, cols = len(mat), len(mat[0])
        q = deque()
        fresh = 0
        # Collect all rotten oranges and count fresh ones
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 2:
                    q.append((i, j))
                elif mat[i][j] == 1:
                    fresh += 1
        # No fresh oranges present
        if fresh == 0:
            return 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        time = 0
        while q and fresh > 0:
            size = len(q)
            for _ in range(size):
                x, y = q.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if (0 <= nx < rows and 0 <= ny < cols and
                            mat[nx][ny] == 1):
                        mat[nx][ny] = 2
                        fresh -= 1
                        q.append((nx, ny))
            time += 1
        return time if fresh == 0 else -1
