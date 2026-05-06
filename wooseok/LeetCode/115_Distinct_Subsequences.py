class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # dp? lcs 변형
        # dp[i][j] => s의 i번째 인덱스까지 확인했을 때 t의 j번째 인덱스까지 완성된 최대 경우의 수
        n, m = len(s), len(t)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 1

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s[i - 1] == t[j - 1]:
                    # 사용하는 경우 + 사용하지 않는 경우
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    # 무조건 사용 불가
                    dp[i][j] = dp[i - 1][j]

        return dp[n][m]
