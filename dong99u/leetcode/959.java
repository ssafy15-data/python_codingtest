package leetcode.leetcode959;

import java.util.*;

public class Solution {

	static final int[][] DIR = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
	static final int EXTENDED = 3;
	static int n;
	static boolean[][] visited;
	static int[][] board;

	public static void main(String[] args) {
		System.out.println(regionsBySlashes(new String[] {"//","/ "}));
	}

	public static int regionsBySlashes(String[] grid) {
		n = grid.length;
		visited = new boolean[n * EXTENDED][n * EXTENDED];

		board = new int[n * EXTENDED][n * EXTENDED];

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < grid[i].length(); j++) {
				if (grid[i].charAt(j) == '\\') {
					board[i * EXTENDED][j * EXTENDED] = 1;
					board[i * EXTENDED + 1][j * EXTENDED + 1] = 1;
					board[i * EXTENDED + 2][j * EXTENDED + 2] = 1;
				} else if (grid[i].charAt(j) == '/') {
					board[i * EXTENDED][j * EXTENDED + 2] = 1;
					board[i * EXTENDED + 1][j * EXTENDED + 1] = 1;
					board[i * EXTENDED + 2][j * EXTENDED] = 1;
				}
			}
		}

		int answer = 0;
		for (int i = 0; i < n * EXTENDED; i++) {
			for (int j = 0; j < n * EXTENDED; j++) {
				if (board[i][j] == 0 && !visited[i][j]) {
					bfs(i, j);
					answer++;
				}
			}
		}

		return answer;
    }

	public static void bfs(int x, int y) {
		Queue<int[]> queue = new ArrayDeque<>();
		queue.add(new int[] {x, y});
		visited[x][y] = true;

		while (!queue.isEmpty()) {
			int[] curr = queue.poll();

			for (int[] d : DIR) {
				int nx = curr[0] + d[0], ny = curr[1] + d[1];

				if (inRange(nx, ny) && board[nx][ny] == 0 && !visited[nx][ny]) {
					queue.add(new int[] {nx, ny});
					visited[nx][ny] = true;
				}
			}
		}
	}

	static boolean inRange(int x, int y) {
		return (0 <= x && x < n * EXTENDED) && (0 <= y && y < n * EXTENDED);
	}
}
