package leetcode.leetcode2076;

public class Solution {
    private int[] parent;
    private int[] rank_;

    public boolean[] friendRequests(int n, int[][] restrictions, int[][] requests) {
        parent = new int[n];
        rank_ = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;

        int Q = requests.length;
        boolean[] ans = new boolean[Q];

        for (int i = 0; i < Q; i++) {
            int u = requests[i][0], v = requests[i][1];
            int pu = find(u), pv = find(v);

            // case 1: 이미 같은 그룹 → 항상 성공
            if (pu == pv) {
                ans[i] = true;
                continue;
            }

            // case 2: 모든 restriction에 대해 위반 여부 검사
            boolean ok = true;
            for (int[] r : restrictions) {
                int px = find(r[0]), py = find(r[1]);
                if ((pu == px && pv == py) || (pu == py && pv == px)) {
                    ok = false;
                    break;
                }
            }

            if (ok) {
                union(pu, pv);  // 이미 루트이므로 직접 union
                ans[i] = true;
            }
            // 위반 시 ans[i]는 default false
        }

        return ans;
    }

    private int find(int x) {
        if (parent[x] != x) parent[x] = find(parent[x]);  // path compression
        return parent[x];
    }

    // a, b는 이미 루트라고 가정
    private void union(int a, int b) {
        if (rank_[a] < rank_[b]) {
            parent[a] = b;
        } else if (rank_[a] > rank_[b]) {
            parent[b] = a;
        } else {
            parent[b] = a;
            rank_[a]++;
        }
    }
}