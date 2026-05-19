package leetcode.leetcode3640;

import java.util.*;

/**
 * 4 <= n <= 10^5 -> 최대 O(nlogn)
 * 이 문제를 brute force로 풀면 O(n^5)?? -> O(n^2)만큼 [l, r] 구간 잡고, O(n^2)만큼 [p, q] 구간 잡아서 O(n)만큼 단조 증가/감소 확인
 * dp
 */
public class Solution {
	static final long MIN_VALUE = -Long.MAX_VALUE;

	public static void main(String[] args) {
		System.out.println(maxSumTrionic(new int[] {0, -2, -1, -3, 0, 2, -1}));
	}
	public static long maxSumTrionic(int[] nums) {
		int n = nums.length;
		long[][] dp = new long[n][4];

		// dp 테이블을 -inf로 초기화
		for (int i = 0; i < n; i++) {
			Arrays.fill(dp[i], MIN_VALUE);
		}

		/**
		 * 조건 충족 시 (k=1,3이면 arr[i-1] < arr[i], k=2면 arr[i-1] > arr[i]):
		 *
		 *   dp[i][k] = max(
		 *       dp[i-1][k]   + arr[i],   // ① 확장 (같은 단계 안에서 한 칸 연장)
		 *       dp[i-1][k-1] + arr[i]    // ② 전이 (이전 단계에서 막 넘어옴)
		 *   )
		 */

		for (int i = 1; i < n; i++) {
			boolean isIncrement = nums[i - 1] < nums[i];
			boolean isDecrement = nums[i - 1] > nums[i];

			// k = 1: 증가 단계
			if (isIncrement) {
				// 확장 (같은 단계 안에서 한 칸 연장)
				long curr = (dp[i - 1][1] != MIN_VALUE) ? dp[i - 1][1] + nums[i] : MIN_VALUE;
				// 새로 시작 (길이 2짜리 증가 부분배열로 출발)
				long next = nums[i - 1] + nums[i];
				dp[i][1] = Math.max(curr, next);
			}

			if (isDecrement) {
				// 확장 (같은 단계 안에서 한 칸 연장)
				long curr = (dp[i - 1][2] != MIN_VALUE) ? dp[i - 1][2] + nums[i] : MIN_VALUE;
				// 전이 (이전 단계에서 막 넘어옴)
				long next = (dp[i-1][1] != MIN_VALUE) ? dp[i-1][1] + nums[i] : MIN_VALUE;
				dp[i][2] = Math.max(curr, next);
			}

			if (isIncrement) {
				long curr = (dp[i - 1][3] != MIN_VALUE) ? dp[i - 1][3] + nums[i] : MIN_VALUE;
				long next = (dp[i - 1][2] != MIN_VALUE) ? dp[i - 1][2] + nums[i] : MIN_VALUE;
				dp[i][3] = Math.max(curr, next);
			}
		}

		long answer = MIN_VALUE;
		for (int i = 0; i < n; i++) {
			answer = Math.max(answer, dp[i][3]);
		}
		return answer;
    }
}
