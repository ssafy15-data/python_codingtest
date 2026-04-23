#include <stdio.h>
#include <string.h>
#pragma warning(disable:4996)

int main(void) {
	char str[1000005], key[40], res[1000005];
	int idx = 0;
	scanf("%s", str);
	scanf("%s", key);
	int l_str = strlen(str);
	int l_key = strlen(key);
	for (int i = 0; i < l_str; i++) {
		res[idx++] = str[i];
		if (str[i] == key[l_key - 1] && idx >= l_key) {
			int c = 0;
			for (int j = 0; j < l_key; j++) {
				if (key[l_key - j - 1] != res[idx - j - 1]) {
					c = 1;
					break;
				}
			}
			if (c == 0) {
				idx -= l_key;
			}
		}
	}
	res[idx] = '\0';
	if (idx == 0) printf("FRULA\n");
	else printf("%s\n", res);
	return 0;
}
