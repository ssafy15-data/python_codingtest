class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        M, N = len(dungeon), len(dungeon[0])
        MAX = int(1e9)
        dp = [[MAX for _ in range(N + 2)] for _ in range(M + 2)]
        
        dp[M + 1][N] = dp[M][N + 1] = 1
        for i in range(M, 0, -1):
            for j in range(N, 0, -1):
                temp = min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i - 1][j - 1]
                if (temp <= 0): temp = 1
                dp[i][j] = temp
        return dp[1][1]