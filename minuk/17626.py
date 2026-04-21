#include <stdio.h>
#include <stdlib.h>
#include <memory.h>
#include <limits.h>
#include <math.h>
#pragma warning(disable:4996)
#define min(x, y) ((x) > (y) ? (y) : (x))
#define max(x, y) ((x) > (y) ? (x) : (y))

int n;
int dp[50010];

int main() {
	scanf("%d", &n);

	dp[1] = 1;
	for (int i = 1; i <= n; i++) {
		dp[i] = dp[1] + dp[i - 1];
		for (int j = 1; j * j <= i; j++) {
			dp[i] = min(dp[i], 1 + dp[i - j * j]);
		}
	}

	printf("%d\n", dp[n]);
	return 0;
}