package leetcode.leetcode68;

import java.util.*;

public class Solution {
	public static void main(String[] args) {
		List<String> answer = fullJustify(
			new String[] {"What","must","be","acknowledgment","shall","be"}, 16
		);

		for (String s : answer) {
			System.out.println(s);
		}
	}
    public static List<String> fullJustify(String[] words, int maxWidth) {
		int n = words.length;

		List<String> line = new ArrayList<>(List.of(words[0]));
		int sum = words[0].length();
		List<String> answer = new ArrayList<>();
		for (int i = 1; i < n; i++) {
			if (sum + 1 + words[i].length() > maxWidth) {
				sum = words[i].length();
				answer.add(getJustifiedLine(line, maxWidth));
				line.clear();
				line.add(words[i]);
			} else {
				sum += 1 + words[i].length();
				line.add(words[i]);
			}

		}
		answer.add(getLastLineJustified(line, maxWidth));

		return answer;
    }

	static String getJustifiedLine(List<String> line, int maxWidth) {
		StringBuilder sb = new StringBuilder();
		if (line.size() == 1) {
			sb.append(line.get(0));
			sb.append(" ".repeat(maxWidth - line.get(0).length()));
			return sb.toString();
		}
		int sumLength = line.stream().mapToInt(String::length).sum();
		int rest = maxWidth - sumLength;

		int k = (int)(rest / (line.size() - 1));
		int l = rest % (line.size() - 1);

		for (int i = 0; i < line.size(); i++) {
			sb.append(line.get(i));
			if (i == line.size() - 1) break;
			sb.append(" ".repeat(k + (i < l ? 1 : 0)));
		}
		return sb.toString();
	}

	static String getLastLineJustified(List<String> line, int maxWidth) {
		StringBuilder sb = new StringBuilder();

		for (int i = 0; i < line.size(); i++) {
			sb.append(line.get(i));
			if (i == line.size() - 1) break;
			sb.append(" ");
		}

		sb.append(" ".repeat(maxWidth - sb.length()));
		return sb.toString();
	}
}