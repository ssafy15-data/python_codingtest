class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        N = len(grid)
        extend_N = N * 3
        mat = [[0 for _ in range(extend_N + 1)] for _ in range(extend_N + 1)]
        for i in range(N):
            for j in range(N):
                if (grid[i][j] == '/'):
                    for offset in range(3):
                        mat[i * 3 + offset][j * 3 + (2 - offset)] = 1
                elif (grid[i][j] == '\\'):
                    for offset in range(3):
                        mat[i * 3 + offset][j * 3 + offset] = 1
        # print(*mat, sep='\n')
        visited = [[0 for _ in range(extend_N + 1)] for _ in range(extend_N + 1)]
        res = 0
        dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
        for i in range(extend_N):
            for j in range(extend_N):
                if (not visited[i][j] and not mat[i][j]):
                    res += 1
                    visited[i][j] = 1
                    stack = [(i, j)]
                    while (stack):
                        x, y = stack.pop()
                        for offset in range(4):
                            cx, cy = x + dx[offset], y + dy[offset]
                            if (not (0 <= cx < extend_N) or not(0 <= cy < extend_N) or visited[cx][cy] or mat[cx][cy]): continue
                            visited[cx][cy] = 1
                            stack.append((cx, cy))
        return res