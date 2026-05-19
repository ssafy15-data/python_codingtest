package leetcode.leetcode3101;

/**
 * 1 <= n <= 10^5 이므로
 * brute force로 풀면 O(n^2) or O(n^3)이라 시간초과 남.
 * 적어도 O(nlogn)이하로 풀기 -> dp?
 */
public class Solution {

	public static void main(String[] args) {
		System.out.println(countAlternatingSubarrays(new int[] {1, 0, 1, 0}));
	}

	public static long countAlternatingSubarrays(int[] nums) {
		int n = nums.length;

		int[] dp = new int[n]; // i번째 인덱스로 끝나는 교대배열의 개수
		dp[0] = 1;

		/**
		 * nums = [0, 1, 0, 1]
		 * dp =>  0  1  0   1
		 *          01 10  01
		 *             010 101
		 *                 0101
		 */
		for (int i = 1; i < n; i++) {
			if (nums[i] != nums[i - 1]) {
				dp[i] = dp[i - 1] + 1;
			} else {
				dp[i] = 1;
			}
		}

		long sum = 0;
		for (int elem : dp) {
			sum += elem;
		}

		return sum;
    }
}
