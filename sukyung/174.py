# Dungeon Game - Hard

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        dp = [[1e9]*(n+1) for _ in range(m+1)]
        # dp[i][j] = (i, j) 칸에 도착했을 때 필요한 최소 체력

        # 초기 (m,n) 칸 비교 위해 설정
        dp[m-1][n] = dp[m][n-1] = 1

        # 도착지에서 출발지로 거꾸로 탐색
        # : 왼쪽이나 위로만 이동 가능하므로 오른쪽, 아래 칸과만 비교하면 됨
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                # 현재 칸에서 필요한 최소 체력: 오른쪽, 아래 칸에서 dungeon[i][j]를 뺀 값 중 더 최소인 값
                dp[i][j] = min(dp[i][j+1], dp[i+1][j]) - dungeon[i][j]
                # 중간에 체력이 1번이라도 0 이하로 떨어지면 안되므로 음수가 나오는 경우 1로 저장
                if dp[i][j] <= 0:
                    dp[i][j] = 1
                
        return dp[0][0]