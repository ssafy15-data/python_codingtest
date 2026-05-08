class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        """
        노드 하나를 아래와 같은 번호의 삼각형 4개로 분리
          0
        1   2
          3
        """
        n = len(grid)
        parent = list(range(4 * n * n))
        rank = [0] * (4 * n * n)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            a = find(a)
            b = find(b)

            if a != b:
                if rank[a] > rank[b]:
                    parent[b] = a
                elif rank[a] < rank[b]:
                    parent[a] = b
                else:
                    parent[b] = a
                    rank[a] += 1

        for i in range(n):
            for j in range(n):
                x = grid[i][j]
                root = 4 * (i * n + j)

                if x == '/':
                    union(root + 0, root + 1)
                    union(root + 2, root + 3)
                elif x == '\\':
                    union(root + 0, root + 2)
                    union(root + 1, root + 3)
                else:  # 공백
                    union(root + 0, root + 1)
                    union(root + 1, root + 2)
                    union(root + 2, root + 3)

                # 오른쪽과 조합
                if j + 1 < n:
                    union(root + 2, 4 * (i * n + (j + 1)) + 1)
                
                # 아래와 조합
                if i + 1 < n:
                    union(root + 3, 4 * ((i + 1) * n + j) + 0)
        
        return sum(find(i) == i for i in range(4 * n * n))
