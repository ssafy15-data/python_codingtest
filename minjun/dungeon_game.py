class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        import heapq

        m = len(dungeon)
        n = len(dungeon[0])

        def big_minus(num1, num2):
            if num1 >= 0 and num2 >= 0:
                return 0
            if num1 < 0 and num2 < 0:
                return min(num1, num2)
            if num1 < 0:
                return num1
            else:
                return num2

        dxys = [(0, 1), (1, 0)]
        fval = big_minus(0, dungeon[0][0])
        pq = [(-fval, -dungeon[0][0], 0, 0)]
        visited = [[-200000]*n for _ in range(m)]

        while pq:
            val, health_val, x, y = heapq.heappop(pq)

            if x == m-1 and y == n-1:
                break

            for dx, dy in dxys:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    nhealth = -health_val + dungeon[nx][ny]
                    nval = big_minus(-val, nhealth)
                    if visited[nx][ny] <= nhealth:
                        visited[nx][ny] = nhealth
                        heapq.heappush(pq, (-nval, -nhealth, nx, ny))
        
        return val+1