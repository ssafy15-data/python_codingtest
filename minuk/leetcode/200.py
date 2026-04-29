class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        M, N = len(grid), len(grid[0])
        dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
        visited = [[0 for j in range(N)] for i in range(M)]
        res = 0
        for i in range(M):
            for j in range(N):
                if (not visited[i][j] and grid[i][j] == "1"):
                    res += 1
                    stack = [(i, j)]
                    while (stack):
                        x, y = stack.pop()
                        for offset in range(4):
                            cx, cy = x + dx[offset], y + dy[offset]
                            if (not (0 <= cx < M and 0 <= cy < N) or visited[cx][cy] or grid[cx][cy] == "0"): continue
                            visited[cx][cy] = 1
                            stack.append((cx, cy))
        
        return res