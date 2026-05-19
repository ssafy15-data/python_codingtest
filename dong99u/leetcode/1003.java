package leetcode.leetcode1003;

import java.util.*;

/**
 * 1 <= n <= 2 * 10^4 이므로 O(n^2) ?? 아래 정도로
 * stack 문제
 * 비교해야할 문자는 'abc'로 최대 3개 밖에 없으니까
 * 따로 배열로 누적해서 검사하지 말고 그냥 다 검사하기.
 */
public class Solution {

	public static void main(String[] args) {
		System.out.println(isValid("aabcbc"));
		System.out.println(isValid("abcabcababcc"));
		System.out.println(isValid("abccba"));
	}
	public static boolean isValid(String s) {
		int n = s.length();
		ArrayDeque<Character> stack = new ArrayDeque<>();

		boolean flag = true;
		for (char c : s.toCharArray()) {
			stack.push(c);
			if (stack.size() >= 3 && stack.peek() == 'c') {
				StringBuilder stackSb = new StringBuilder();

				for (int i = 0; i < 3; i++) {
					stackSb.append(stack.pop());
				}

				if (!"cba".equals(stackSb.toString())) { // abc로 만들 수 없다면 정답 x
					return false;
				}
			}
		}

		if (!stack.isEmpty()) {
			flag = false;
		}

		return flag;
    }
}
