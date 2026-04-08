#include <stdio.h>
#pragma warning(disable:4996)
int l[301] = { 0, };
int dp[301] = { 0, };

int DP(int n) {
	if (n == 0) return 0;
	else if (n == 1) return l[1];
	else if (n == 2) return l[1] + l[2];
	else if (dp[n] != 0) return dp[n];
	else {
		if (DP(n - 3) + l[n - 1] + l[n] > DP(n - 2) + l[n]) {
			dp[n]= DP(n - 3) + l[n - 1] + l[n];
			return dp[n];
		}
		else {
			dp[n]= DP(n - 2) + l[n];
			return dp[n];
		}
	}
}
int main() {
	int n;
	scanf("%d", &n);
	for (int i = 1; i < n + 1; i++) {
		scanf("%d", &l[i]);
	}
	printf("%d", DP(n));
	return 0;
}