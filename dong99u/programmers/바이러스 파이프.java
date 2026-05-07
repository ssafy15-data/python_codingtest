package programmers.programmers468373;

import java.util.*;

/**
 * 1. 문제 이해
 *
 * 트리 구조 (n ≤ 100), 초기 감염 노드 1개
 * type 1/2/3 중 하나를 골라 그 type 간선으로 BFS 전파를 최대 k번 (k ≤ 10) 반복
 * 최종 감염 노드 수의 최댓값
 *
 * 2. Brute Force 설계 (백트래킹)
 * 상태 트리:
 *                    backtrack(0)
 *               /         |         \
 *           type=1      type=2      type=3
 *          (BFS전파)   (BFS전파)   (BFS전파)
 *         /  |  \      /  |  \     /  |  \
 *        1   2   3    1   2   3   1   2   3
 *        ⋮
 *        (깊이 k)
 *
 * 각 분기에서 type 3가지 중 하나 선택 → 중복 순열
 * 파라미터: count (현재까지 행동 횟수)
 * 부수 상태: visited[] (감염 여부)
 * 한 번의 행동(BFS) 효과: 감염된 노드들에서 시작하는 multi-source BFS로 같은 type 간선을 따라 전파
 *
 * 3. 복잡도 분석
 *
 * 분기 수: O(3^k) = O(3^10) ≈ 5.9 × 10^4
 * 각 분기의 BFS: O(V + E) = O(n) (트리이므로 E = n-1)
 * 총: O(3^k · n) ≈ 6 × 10^6 → Java로 충분히 통과
 *
 * 4. 메모이제이션 가능성 검토
 *
 * 상태 공간이 DAG임
 * 같은 상태가 여러 경로로 도달? → 이론상 가능 (예: A→B와 B→A가 같은 visited 집합으로 수렴 가능)
 * 그러나 memo 키가 (count, visited 집합)이 되어야 하는데, n=100이라 비트마스크 표현이 비실용적
 * 결론: 메모이제이션은 히트율이 낮고, 3^k 자체가 충분히 작아 가지치기 + 직접 탐색으로 통과 가능
 *
 * 5. 핵심 구현 포인트
 * ① Multi-source BFS
 *
 * 매 행동 시 "현재 감염된 모든 노드"를 큐에 넣고 시작 → 같은 type 간선을 따라 전파
 *
 * ② Bulk undo (백트래킹 복구)
 *
 * BFS는 여러 노드의 visited를 한 번에 변경하므로, 새로 감염된 노드 리스트를 반환해서 일괄 복구
 * List<Integer> newInfected = bfs(type);
 * // 재귀 호출
 * for (int i : newInfected) visited[i] = false;  // 일괄 undo
 *
 * ③ 자연 가지치기
 *
 * newInfected.isEmpty()면 continue → 해당 type은 무의미한 선택이므로 스킵
 *
 * ④ 누적 결과 처리 (방식 B - backward)
 *
 * framework의 인자/리턴값 판별 기준 적용:
 *
 * acc(현재까지 감염 수)는 기저 조건 판정에도, 가지치기에도 불필요
 * 따라서 acc는 인자가 아닌 리턴값으로 수집 (방식 B)
 * 리턴값 = newInfected.size() + backtrack(count + 1) 누적
 *
 *
 * ⑤ 최초 감염 노드 보정
 *
 * backtrack(0)은 "행동 이후 새로 감염된 수"만 리턴 → 최초 감염 노드 1개를 마지막에 더해줌
 * return backtrack(0) + 1;
 */
public class Solution {
	static List<List<int[]>> graph;
	static int n;
	static int infection;
	static int k;
	static boolean[] visited;


	public static int solution(int n, int infection, int[][] edges, int k) {
    	Solution.n = n; Solution.k = k; Solution.infection = infection;
		visited = new boolean[n + 1];

		graph = new ArrayList<>();
		visited[infection] = true;
		for (int i = 0; i <= n; i++) {
			graph.add(new ArrayList<>());
		}

		for (int[] edge : edges) {
			int u = edge[0], v = edge[1], type = edge[2];
			graph.get(u).add(new int[] {v, type});
			graph.get(v).add(new int[] {u, type});
		}

		return backtrack(0) + 1;
	}

	static int backtrack(int count) {
		if (count == k)
			return 0;

		int best = 0;
		for (int type = 1; type <= 3; type++) {
			List<Integer> newInfected = bfs(type);

			if (newInfected.isEmpty()) continue;

			best = Math.max(best, newInfected.size() + backtrack(count + 1));
			for (int i : newInfected) visited[i] = false;
		}
		return best;
	}

	static List<Integer> bfs(int type) {
		Queue<Integer> queue = new ArrayDeque<>();
		List<Integer> result = new ArrayList<>(); // 새로 감염된 노드들

		for (int i = 1; i <= n; i++) {
			if (visited[i]) queue.add(i);
		}

		while (!queue.isEmpty()) {
			int curr = queue.poll();

			for (int[] next : graph.get(curr)) {
				int nextNode = next[0], nextType = next[1];
				if (!visited[nextNode] && nextType == type) {
					visited[nextNode] = true;
					queue.add(nextNode);
					result.add(nextNode);
				}
			}
		}
		return result;
	}

}
