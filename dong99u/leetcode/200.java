package leetcode.leetcode200;

import java.util.*;

public class Solution {
	static int n, m; // 행 크기 m, 열 크기 n
	static int[] dxs = {1, 0, -1, 0};
	static int[] dys = {0, 1, 0, -1};

	public static int numIslands(char[][] grid) {
		m = grid.length;
		n = grid[0].length;

		boolean[][] visited = new boolean[m][n];

		int answer = 0;
		for (int i = 0; i < m; i++) {
			for (int j = 0; j < n; j++) {
				if (grid[i][j] == '1' &&!visited[i][j]) {
					dfs(i, j, grid, visited);
					answer++;
				}
			}
		}

		return answer;

    }

	static void dfs(int x, int y, char[][] grid, boolean[][] visited) {
		visited[x][y] = true;

		for (int i = 0; i < 4; i++) {
			int nx = x + dxs[i];
			int ny = y + dys[i];

			if (canGo(nx, ny, grid, visited)) {
				dfs(nx, ny, grid, visited);
			}

		}

	}

	static boolean canGo(int x, int y, char[][] grid, boolean[][] visited) {
		return inRange(x, y) && !visited[x][y] && grid[x][y] == '1';
	}

	static boolean inRange(int x, int y) {
		return (0 <= x && x < m) && (0 <= y && y < n);
	}
}
