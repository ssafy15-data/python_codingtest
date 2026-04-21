#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>
#include <math.h>
#pragma warning(disable:4996)
#define swap(x,y,t) ((t)=(x),(x)=(y),(y)=(t))
#define max(x, y) ((x) > (y) ? (x) : (y))
#define min(x, y) ((x) > (y) ? (y) : (x))

int parent[500001];

int getParent(int a) {
	if (a == parent[a])
		return a;
	return parent[a] = getParent(parent[a]);
}

void unionFind(int a, int b) {
	a = getParent(a);
	b = getParent(b);
	if (a != b) {
		if (a < b) parent[b] = a;
		else parent[a] = b;
	}
}


int main() {
    int n, k;
    scanf("%d %d", &n, &k);

    for (int i = 0; i < n; i++) {
        parent[i] = i;
    }
	
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++) {
			int data;
			scanf("%d", &data);
			if (data) unionFind(i, j);
		}
	}
	
	int data[1002];
    for (int i = 1; i <= k; i++) {
    	scanf("%d", &data[i]);
    }
    for (int i = 1; i < k; i++) {
    	if (getParent(data[i]) != getParent(data[i + 1])) {
    		printf("NO\n");
    		return 0;
    	}
    }

    printf("YES\n");

    return 0;
}