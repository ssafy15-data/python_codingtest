package leetcode.leetcode115;

import java.util.*;

/**
 * 문제
 * 문자열 s에서 부분수열로 t를 만드는 방법의 수를 구하기.
 * 1. 처음 생각 (백트래킹부터 시작)
 * s의 각 글자에 대해 선택/비선택 두 분기로 brute force.
 *
 * 상태: (idx, count) — s에서 idx번째까지 봤고, t의 count글자까지 매칭 완료
 * 선택: s[idx] == t[count]일 때만 가능 → (idx+1, count+1)
 * 비선택: 항상 가능 → (idx+1, count)
 *
 * 2. 복잡도 분석 → 최적화 결정
 *
 * Brute force: 분기수 2 × 깊이 n → O(2ⁿ), n=1000이면 타임아웃.
 * 상태 공간: idx, count 모두 단조 증가 → DAG → 메모이제이션 가능
 * 같은 (idx, count)에 여러 경로 도달 → 메모이제이션 효과 큼
 *
 * → 백트래킹 + 메모이제이션 = O(n·k)
 */

public class Solution {
	static String s;
	static String t;
	static int n;
	static int k;
	static int[][] memo;

	public static void main(String[] args) {
		System.out.println(numDistinct("rabbbit", "rabbit"));
	}
	public static int numDistinct(String s, String t) {
		Solution.s = s; Solution.t = t;
		n = s.length();
		k = t.length();
		memo = new int[n + 1][k + 1];
		for (int i = 0; i <= n; i++) {
			Arrays.fill(memo[i], -1);
		}

		return backtrack(0, 0);
    }

	static int backtrack(int idx, int count) {
		if (memo[idx][count] != -1) return memo[idx][count];
		if (idx == n) {
			if (count != k) return 0;
		}
		if (count == k) return 1;

		int result = 0;
		if (s.charAt(idx) == t.charAt(count)) {
			result += backtrack(idx + 1, count + 1);
		}
		result += backtrack(idx + 1, count);

		memo[idx][count] = result;
		return memo[idx][count];
	}

}
