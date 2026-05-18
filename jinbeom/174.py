class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n, m = len(dungeon), len(dungeon[0])
        dp = [[1e9] * m for _ in range(n)]

        dp[-1][-1] = 1 + max(0, -dungeon[-1][-1])
        for r in range(n - 2, -1, -1):
            dp[r][-1] = max(1, dp[r + 1][-1] - dungeon[r][-1])
        for c in range(m - 2, -1, -1):
            dp[-1][c] = max(1, dp[-1][c + 1] - dungeon[-1][c])

        for r in range(n - 2, -1, -1):
            for c in range(m - 2, -1, -1):
                dp[r][c] = max(1, min(dp[r][c + 1], dp[r + 1][c]) - dungeon[r][c])

        return dp[0][0]