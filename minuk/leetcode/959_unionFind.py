class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        N = len(grid)
        visited = [[[0, 0] for _ in range(N + 1)] for _ in range(N + 1)]
        # d=0: 상, d=1: 우, d=2: 하, d=3: 좌
        parent = [i for i in range(4 * N * N)]
        def getParent(a):
            # print(x, y, d)
            if (parent[a] != a): parent[a] = getParent(parent[a])
            return parent[a]
        def unionFind(a, b):
            a, b = getParent(a), getParent(b)
            if (a != b):
                parent[b] = a
        
        for x in range(N):
            for y in range(N):
                val = (x * N + y) << 2
                if (x < N - 1):
                    unionFind(val | 2, val + 4 * N)
                if (y < N - 1):
                    unionFind(val | 1, (val + 4) | 3)
                if (grid[x][y] == ' '):
                    for d in range(3):
                        unionFind(val | d, val | (d + 1))
                elif (grid[x][y] == '/'):
                    unionFind(val | 0, val | 3)
                    unionFind(val | 1, val | 2)
                else:
                    unionFind(val | 0, val | 1)
                    unionFind(val | 2, val | 3)

        res = 0
        for i in range(4 * N * N):
            if (getParent(i) == i): res += 1
        return res