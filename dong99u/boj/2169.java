import java.util.*;
import java.io.*;

public class Main {
	// 가로 세로 크기
	static int n;
	static int m;
	static int[][] grid; // 격자

	static final int L = 0;
	static final int R = 1;
	static final int D = 2;
	static final int INF = (int) 1e9;

	public static void main(String[] args) throws IOException {
		init();

		int[][][] dp = new int[n][m][3];
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				Arrays.fill(dp[i][j], -INF);
			}
		}
		dp[0][0][D] = grid[0][0];

		// 0행: 오른쪽 방향으로만 확장 (시작점에서 왼쪽은 갈 수 없음)
        for (int j = 1; j < m; j++) {
            int prev = Math.max(dp[0][j - 1][R], dp[0][j - 1][D]);
            if (prev != -INF) {
                dp[0][j][R] = grid[0][j] + prev;
            }
        }

		for (int i = 1; i < n; i++) {
			for (int j = 0; j < m; j++) {
				dp[i][j][D] = grid[i][j] + Arrays.stream(dp[i - 1][j]).max().getAsInt();
				if (inRange(i, j - 1)) {
					dp[i][j][R] = grid[i][j] + Math.max(dp[i][j - 1][D], dp[i][j - 1][R]);
				}
			}
			for (int j = m - 1; j >= 0; j--) {
				if (inRange(i, j + 1)) {
					dp[i][j][L] = grid[i][j] + Math.max(dp[i][j + 1][D], dp[i][j + 1][L]);
				}
			}
		}

		int answer = Arrays.stream(dp[n - 1][m - 1]).max().getAsInt();
		System.out.println(answer);

	}

	static boolean inRange(int x, int y) {
		return (0 <= x && x < n) && (0 <= y && y < m);
	}

	static void init() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());

		grid = new int[n][m];

		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < m; j++) {
				grid[i][j] = Integer.parseInt(st.nextToken());
			}
		}
	}
}
