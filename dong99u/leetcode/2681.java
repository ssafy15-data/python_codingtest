package leetcode.leetcode2681;

import java.util.Arrays;

public class Solution {
	/**
	 * nums = [2, 1, 4]에서 4가 최댓값이 되는 부분집합은 {4}, {1, 4}, {2, 1, 4}로 총 3개
	 * 4가 최댓값이란 조건이 다른 나머지 원소들에 제약을 건다.
	 * 정렬 -> [1, 2, 4]라면 최대값이 4일때 자기 자신을 포함한 그 앞에 모든 숫자들이 올 수 있다.
	 * 그리고 그 중에 최소값은 맨 앞에 있는 원소.
	 * 정렬된 배열에서 nums[j]를 최댓값으로 고정 -> 부분집합에 들어올 수 있는 후보는 nums[0...j](자기자신 포함)
	 * nums[j]는 반드시 포함, nums[0...j-1] 중에서는 선택.
	 * min은 그 부분집합에서 가장 작은 인덱스의 원소
	 * min도 i번째 수로 고정시킨다면, 부분집합의 개수는 2 ^ (j - i - 1)개.
	 *
	 * [1, 2, 4]를 예시로 한다면 최대값을 j = 2로 고정했을 때,
	 *
	 * 1. i = 0,
	 * 	2 ^ (j - i - 1) = 2 -> {1, 4}, {1, 2, 4}
	 * 2. i = 1,
	 * 	2 ^ (j - i - 1) = 1 -> {2, 4}
	 * 3. i = 2,
	 * 	2 ^ (j - i - 1) = 1/2 -> i = j 일때, 1로 처리해야한다. {4}
	 *
	 * 하지만 이걸 브루트 포스로 하면 O(n ^ 2) -> n <= 10 ^ 5 이므로 TLE 난다.
	 *
	 * 여기까지 정리하자면, 구하고자 하는 답을 식으로 만들면
	 *
	 * answer = (n - 1)∑j=0  j∑i=0 nums[j] ^ 2 * nums[i] * 2 ^ (j - i - 1)
	 *
	 * 그럼 미리 O(n)에 걸쳐 미리 값을 구해놓으면 해결되지 않을까?
	 * answer 뒤쪽에 식을 다시 보면
	 *
	 * S_j = 정렬된 배열에서 nums[j]를 최댓값으로 고정했을 때, 모든 가능한 (min × 부분집합 개수)의 합
	 * S_j = (j - 1)∑i=0 nums[i] (nums[i] * 2 ^ (j - i - 1) 라고 했을 때,
	 *
	 * 점화식으로 전개
	 * S_1 = nums[0] · 2^0
	 * S_2 = nums[0] · 2^1 + nums[1] · 2^0
	 * S_3 = nums[0] · 2^2 + nums[1] · 2^1 + nums[2] · 2^0
	 *
	 * 즉 S_{j + 1} = 2 * S_j + nums[j]
	 *
	 * 누적합 처럼 배열로 미리 만들어 놓을 수가 있다.
	 */

	static final int MOD = (int)1e9 + 7;

	public static void main(String[] args) {
		System.out.println(sumOfPower(new int[] {2, 1, 4}));
	}
	public static int sumOfPower(int[] nums) {
        int n = nums.length;
        Arrays.sort(nums);

        long answer = 0L;
        long S = 0L;  // S_j: nums[j]를 max로 고정 시 (min × 부분집합 개수)의 합

        for (int j = 0; j < n; j++) {
            long val = nums[j];
            long sq = (val * val) % MOD;          // nums[j]^2

            // 1. i < j 항: nums[j]^2 · S_j
            answer = (answer + sq * S) % MOD;

            // 2. i = j 항: nums[j]^3 (자기 자신만으로 이루어진 부분집합)
            answer = (answer + sq * val) % MOD;

            // 3. 다음 단계를 위해 S 갱신: S_{j+1} = 2·S_j + nums[j]
            S = (2 * S + val) % MOD;
        }

        return (int) answer;
    }
}
