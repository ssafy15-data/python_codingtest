#include <stdio.h>
#include <memory.h>
//#include <limits.h>
#pragma warning(disable:4996)
#define max(x, y) ((x) > (y) ? (x) : (y))

const long long LLONG_MIN = -2e9;
int n, m;
long long int map[1002][1002], dp[4][1002][1002];
int dx[5] = {0, 0, 1}, dy[5] = {-1, 1, 0}, ddir[5] = {0, 1, 2};
int visit[1002][1002];

long long int DP(int dir, int i, int j) {
	if (i <= 0 || i > n || j <= 0 || j > m) return LLONG_MIN;
	if (i == n && j == m) return map[i][j];
	if (dp[dir][i][j] != LLONG_MIN) return dp[dir][i][j];
	visit[i][j] = 1;
	long long int res = LLONG_MIN;
	for (int t = 0; t < 3; t++) {
		int x = dx[t] + i;
		int y = dy[t] + j;
		int d = ddir[t];
		if (!visit[x][y]) res = max(res, DP(d, x, y));
	}
	visit[i][j] = 0;
	res += map[i][j];
	dp[dir][i][j] = res;
	return dp[dir][i][j];
}

int main(void) {
	scanf("%d %d", &n, &m);
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= m; j++) {
			scanf("%lld", &map[i][j]);
			for (int k = 0; k < 3; k++) dp[k][i][j] = LLONG_MIN;
		}
	}
	printf("%lld\n", DP(0, 1, 1));
	return 0;
}
