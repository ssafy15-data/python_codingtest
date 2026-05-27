package leetcode.leetcode3722;

import java.util.*;

public class Solution {
    public static String lexSmallest(String s) {
        int n = s.length();

        String answer = s;

        for (int k = 1; k <= n; k++) {
            // 1. 앞 k개 reverse
            String prefixReversed = new StringBuilder(s.substring(0, k))
                    .reverse()
                    .toString()
                    + s.substring(k);

            if (prefixReversed.compareTo(answer) < 0) {
                answer = prefixReversed;
            }

            // 2. 뒤 k개 reverse
            String suffixReversed = s.substring(0, n - k)
                    + new StringBuilder(s.substring(n - k))
                    .reverse()
                    .toString();

            if (suffixReversed.compareTo(answer) < 0) {
                answer = suffixReversed;
            }
        }

        return answer;
    }
}