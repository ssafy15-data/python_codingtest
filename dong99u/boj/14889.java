import java.util.*;
import java.io.*;

public class Main {
	static final int MAX_VALUE = (int) 1e9;

    static int n;
    static int[][] grid;
    static boolean[] inA;

    public static void main(String[] args) throws IOException {
        init();
        inA[0] = true;
        int answer = splitTeams(1, 1);
        System.out.println(answer);
    }

    /**
     * 현재 inA 상태에서, start 이후를 A팀에 어떻게 채우든
     * 얻을 수 있는 "최소 diff"를 리턴.
     */
    static int splitTeams(int start, int count) {
        // 기저: A팀이 다 차면 이 분할에 대한 diff가 바로 답
        if (count == n / 2) {
            return getDiff();
        }

        int best = MAX_VALUE;
        for (int i = start; i < n; i++) {
            inA[i] = true;
            int sub = splitTeams(i + 1, count + 1);
            inA[i] = false;

            if (sub < best) best = sub;
        }
        return best;
    }

    static int getDiff() {
        int sumA = 0, sumB = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int s = grid[i][j] + grid[j][i];
                if (inA[i] && inA[j])        sumA += s;
                else if (!inA[i] && !inA[j]) sumB += s;
            }
        }
        return Math.abs(sumA - sumB);
    }

    static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        grid = new int[n][n];
        inA = new boolean[n];

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                grid[i][j] = Integer.parseInt(st.nextToken());
            }
        }
    }
}