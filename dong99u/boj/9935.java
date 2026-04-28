import java.util.*;
import java.io.*;

public class Main {
	static String arr;
	static String explosiveStr;
	static int n;
	static int m;
	public static void main(String[] args) throws IOException {
		init();

		StringBuilder stack = new StringBuilder();

		for (int i = 0; i < n; i++) {
			stack.append(arr.charAt(i));

			if (stack.length() >= m) {
				String top = stack.substring(stack.length() - m);
				if (top.equals(explosiveStr)) {
					stack.delete(stack.length() - m, stack.length());  // pop m개
				}
			}
		}

		System.out.println(stack.isEmpty() ? "FRULA" : stack.toString());
	}

	static void init() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		arr = br.readLine();
		n = arr.length();
		explosiveStr = br.readLine();
		m = explosiveStr.length();
	}
}
