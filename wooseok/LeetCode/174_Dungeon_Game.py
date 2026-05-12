class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        """
        단순 숫자 계산으로 하면 예외 케이스 생길 수 있음
        1로 시작 -> -를 만나면 +로, +를 만나면 -로 해서 연산하면? -> 역방향 DP
        """
        INF = int(1e9)

        n = len(dungeon)
        m = len(dungeon[0])

        dp = [[INF] * (m + 1) for _ in range(n + 1)]
        dp[n-1][m] = 1
        dp[n][m-1] = 1
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                min_hp = min(dp[i + 1][j], dp[i][j + 1])
                dp[i][j] = min_hp - dungeon[i][j] if (min_hp - dungeon[i][j]) > 0 else 1
        
        return dp[0][0]