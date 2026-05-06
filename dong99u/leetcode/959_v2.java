package leetcode.leetcode959;

public class SolutionUnionFind {

    static int[] parent;
    static int[] rank_;
    static int n;

    public static int regionsBySlashes(String[] grid) {
        n = grid.length;
        int total = 4 * n * n;
        parent = new int[total];
        rank_ = new int[total];
        for (int i = 0; i < total; i++) parent[i] = i;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int base = 4 * (i * n + j); // 셀 (i,j)의 첫 노드 인덱스
                // 0: N, 1: E, 2: S, 3: W
                char c = grid[i].charAt(j);

                // ① 셀 내부 결합
                if (c == ' ') {
                    union(base + 0, base + 1);
                    union(base + 1, base + 2);
                    union(base + 2, base + 3);
                } else if (c == '/') {
                    union(base + 0, base + 3); // N + W
                    union(base + 1, base + 2); // E + S
                } else if (c == '\\') {
                    union(base + 0, base + 1); // N + E
                    union(base + 2, base + 3); // S + W
                }

                // ② 인접 셀 결합
                if (j + 1 < n) {
                    int rightBase = 4 * (i * n + (j + 1));
                    union(base + 1, rightBase + 3); // E ↔ 옆 셀의 W
                }
                if (i + 1 < n) {
                    int downBase = 4 * ((i + 1) * n + j);
                    union(base + 2, downBase + 0); // S ↔ 아래 셀의 N
                }
            }
        }

        // 루트의 개수 = 영역의 개수
        int regions = 0;
        for (int i = 0; i < total; i++) {
            if (find(i) == i) regions++;
        }
        return regions;
    }

    static int find(int x) {
        if (parent[x] != x) parent[x] = find(parent[x]); // 경로 압축
        return parent[x];
    }

    static void union(int x, int y) {
        int rx = find(x), ry = find(y);
        if (rx == ry) return;
        // rank 기반 합치기
        if (rank_[rx] < rank_[ry]) parent[rx] = ry;
        else if (rank_[rx] > rank_[ry]) parent[ry] = rx;
        else { parent[ry] = rx; rank_[rx]++; }
    }

    public static void main(String[] args) {
        System.out.println(regionsBySlashes(new String[]{" /", "/ "}));   // 2
        System.out.println(regionsBySlashes(new String[]{" /", "  "}));   // 1
        System.out.println(regionsBySlashes(new String[]{"/\\","\\/"})); // 5
        System.out.println(regionsBySlashes(new String[]{"//", "/ "}));   // 3
    }
}