#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <time.h>
#pragma warning(disable:4996)

int min=2000000000;
int mat1[21][21], mat2[21], mat3[21];
int result1[21],result2[21];
int sum1, sum2, sum;

void z2(int n) {
	int idx = 1;
	for (int i = 1; i <= n; i++) {
		int c = 0;
		for (int j = 1; j <= n/2; j++) {
			if (result1[j] == i) c = 1;
		}
		if (c == 0) result2[idx++] = i;
	}
	for (int i = 1; i <= n / 2; i++) {
		for (int j = 1; j <= n / 2; j++) {
			if (i == j) continue;
			sum1 += mat1[result1[i]][result1[j]];
			sum2 += mat1[result2[i]][result2[j]];
			//printf("%d %d\n", mat1[result1[i]][result1[j]], mat1[result2[i]][result2[j]]);
		}				    
	}
}


void z(int k, int count,int n) {
	if (result1[1] == 1) return;
	if (count == n/2 + 1) {
		sum1 = 0;
		sum2 = 0;
		z2(n);
		sum = sum1 > sum2 ? sum1 - sum2 : sum2 - sum1;
		/*
		//printf("%d %d %d\n", sum1, sum2, sum);
		for (int i = 1; i <= n/2; i++) {
			printf("%d ", result1[i]);
		}
		for (int i = 1; i <= n/2; i++) {
			printf("%d ", result2[i]);
		}
		puts("");
		*/
		min = min < sum ? min : sum;
		return;
	}
	
	for (int i = k; i <= n; i++) {
		if (mat2[i]) continue;
		result1[count] = i;
		mat2[i] = 1;
		z(i + 1, count + 1, n);
		result1[count] = 0;
		mat2[i] = 0;
	}
}

int main() {
	int n;
	scanf("%d ", &n);
	
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++) {
			scanf("%d", &mat1[i][j]);
		}
	}
	z(1, 1, n);
	printf("%d\n", min);
	return 0;
}