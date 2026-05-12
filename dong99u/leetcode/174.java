package leetcode.leet174;

public class Solution {
	public int calculateMinimumHP(int[][] dungeon) {
        int m = dungeon.length;
        int n = dungeon[0].length;

        // dp[i][j] = (i, j)에 진입할 때 필요한 최소 HP
        int[][] dp = new int[m][n];

        // 끝 칸: 진입 후 HP가 최소 1이어야 하므로
        //   dungeon[m-1][n-1]이 음수면 1 - 그 값이 필요
        //   양수/0이면 진입 시 1만 있으면 충분
        dp[m - 1][n - 1] = Math.max(1, 1 - dungeon[m - 1][n - 1]);

        // 마지막 행: 오른쪽 칸으로만 갈 수 있음
        for (int j = n - 2; j >= 0; j--) {
            dp[m - 1][j] = Math.max(1, dp[m - 1][j + 1] - dungeon[m - 1][j]);
        }

        // 마지막 열: 아래쪽 칸으로만 갈 수 있음
        for (int i = m - 2; i >= 0; i--) {
            dp[i][n - 1] = Math.max(1, dp[i + 1][n - 1] - dungeon[i][n - 1]);
        }

        // 나머지: 아래/오른쪽 중 더 쉬운 쪽 선택
        for (int i = m - 2; i >= 0; i--) {
            for (int j = n - 2; j >= 0; j--) {
                int need = Math.min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j];
                dp[i][j] = Math.max(1, need);
            }
        }

        return dp[0][0];
    }
}
