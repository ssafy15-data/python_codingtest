package swea.swea1855;

import java.util.*;
import java.io.*;

public class Solution {
	static int n;
	static int[] arr;
	static int[] parent;
	static List<List<Integer>> children;
	static int[] depths;

	static BufferedReader br;

	public static void main(String[] args) throws IOException {
		br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine());

		StringBuilder sb = new StringBuilder();
		for (int tc = 1; tc <= t; tc++) {
			init();
			children = new ArrayList<>();
			for (int i = 0; i <= n; i++) {
				children.add(new ArrayList<>());
			}

			for (int i = 2; i <= n ; i++) {
				int u = i, v = arr[i - 2];
				children.get(v).add(u);
				parent[u] = v;
			}

			long answer = bfs(children);
			sb.append("#").append(tc).append(" ").append(answer).append("\n");

		}

		System.out.println(sb);
	}

	static int getLCA(int a, int b) {
		if (depths[a] < depths[b]) { // depths[a] > depths[b]로 치환.
			int tmp = a; a = b; b = tmp;
		}

		int diff = depths[a] - depths[b];
		for (int i = 0; i < diff; i++) {
			a = parent[a];
		}

		while (a != b) {
			a = parent[a];
			b = parent[b];
		}

		return a;
	}

	static int getDist(int a, int b) {
		return depths[a] + depths[b] - 2 * depths[getLCA(a, b)];
	}

	static long bfs(List<List<Integer>> children) {
		Queue<int[]> queue = new ArrayDeque<>();
		queue.add(new int[] {1, 0});

		List<Integer> paths = new ArrayList<>();
		while (!queue.isEmpty()) {
			int[] curr = queue.poll();
			int currNode = curr[0], currDepth = curr[1];
			paths.add(currNode);

			depths[currNode] = currDepth;
			for (Integer nextNode : Solution.children.get(currNode)) {
				queue.add(new int[] {nextNode, currDepth + 1});
			}
		}

		long result = 0;
		for (int i = 1; i < paths.size(); i++) {
			result += getDist(paths.get(i - 1), paths.get(i));
		}

		return result;
	}

	static void init() throws IOException {
		n = Integer.parseInt(br.readLine());
		String line = br.readLine();   // 줄은 일단 소비
		if (n > 1) {
			// 이때만 파싱
			arr = Arrays.stream(line.split(" "))
				.mapToInt(Integer::parseInt)
				.toArray();
		} else {
			arr = new int[0];          // 빈 배열
		}
		parent = new int[n + 1];
		depths = new int[n + 1];

	}

}
