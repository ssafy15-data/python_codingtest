class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        visit = [[[False] * 4 for _ in range(n)] for _ in range(n)]

        direction = {('/', 0): ((0, 0, 3), (-1, 0, 2)),
                     ('/', 1): ((0, 1, 2), (0, 0, 1)),
                     ('/', 2): ((1, 0, -2), (0, 0, -1)),
                     ('/', 3): ((0, 0, -3), (0, -1, -2)),
                     ('\\', 0): ((0, 0, 1), (-1, 0, 2)),
                     ('\\', 1): ((0, 1, 2), (0, 0, -1)),
                     ('\\', 2): ((1, 0, -2), (0, 0, 1)),
                     ('\\', 3): ((0, 0, -1), (0, -1, -2)),
                     (' ', 0): ((0, 0, 1), (0, 0, 3), (-1, 0, 2)),
                     (' ', 1): ((0, 1, 2), (0, 0, -1), (0, 0, 1)),
                     (' ', 2): ((1, 0, -2), (0, 0, 1), (0, 0, -1)),
                     (' ', 3): ((0, 0, -1), (0, -1, -2), (0, 0, -3)),
                     }

        ret = 0
        for r in range(n):
            for c in range(n):
                for k in range(4):
                    if visit[r][c][k]: continue
                    q = [(r, c, k)]
                    visit[r][c][k] = True
                    ret += 1
                    tmp = []
                    while q:
                        x, y, l = q.pop()
                        for dx, dy, dl in direction[(grid[x][y], l)]:
                            if 0 <= x + dx < n and 0 <= y + dy < n and not visit[x + dx][y + dy][l + dl]:
                                q.append((x + dx, y + dy, l + dl))
                                visit[x + dx][y + dy][l + dl] = True
        return ret
