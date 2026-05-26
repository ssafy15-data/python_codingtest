package leetcode.leetcode207;

import java.util.*;

public class Solution {
	public static void main(String[] args) {
		System.out.println(canFinish(2, new int[][] {{1, 0}, {0, 1}}));

	}

	public static boolean canFinish(int numCourses, int[][] prerequisites) {
		ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
		int[] inDegrees = new int[numCourses]; // in-degree

		// 빈 그래프 초기화 (인접 리스트)
		for (int i = 0; i < numCourses; i++) {
			graph.add(new ArrayList<>());
		}

		for (int[] prerequisite : prerequisites) {
			int u = prerequisite[0];
			int v = prerequisite[1];

			graph.get(u).add(v); // u -> v 로 가는 형태
			inDegrees[v]++;
		}

		ArrayDeque<Integer> queue = new ArrayDeque<>();
		for (int i = 0; i < numCourses; i++) {
			if (inDegrees[i] == 0) {
				queue.offer(i);
			}
		}

		while (!queue.isEmpty()) {
			int now = queue.poll();
			for (Integer next : graph.get(now)) {
				if (--inDegrees[next] == 0) {
					queue.offer(next);
				}
			}
		}

		return Arrays.stream(inDegrees).allMatch(x -> x == 0);
	}
}
