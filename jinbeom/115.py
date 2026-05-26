class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        dp = [[0] * m for _ in range(n)]

        dp[n - 1][m - 1] = int(s[n - 1] == t[m - 1])
        for i in range(n - 2, -1, -1):
            dp[i][m - 1] = int(s[i] == t[m - 1]) + dp[i + 1][m - 1]

        for i in range(n - 2, -1, -1):
            for j in range(m - 1):
                dp[i][j] = dp[i + 1][j] + dp[i + 1][j + 1] * (s[i] == t[j])

        return dp[0][0]