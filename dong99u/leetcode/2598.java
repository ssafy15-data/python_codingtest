package leetcode.leetcode2597;

public class Solution {

	public static int findSmallestInteger(int[] nums, int value) {
        int[] count = new int[value];
        for (int x : nums) {
            int r = ((x % value) + value) % value;
            count[r]++;
        }

        int mex = 0;
        while (count[mex % value] > 0) {
            count[mex % value]--;
            mex++;
        }
        return mex;
    }
}
