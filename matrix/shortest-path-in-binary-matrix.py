class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        direction = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]
        queue = deque([(0, 0, 1)])
        grid[0][0] = 1

        while queue:
            r, c, distance = queue.popleft()
            if r == n-1 and c == n-1:
                return distance
            for dr, dc in direction:
                nr = r + dr
                nc = c + dc
                if 0 <= nr <= n-1 and 0 <= nc <= n-1 and grid[nr][nc] == 0:
                    queue.append((r+dr, c+dc, distance+1))
                    grid[r+dr][c+dc] = 1
        
        return -1
        