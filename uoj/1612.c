#include <stdio.h>

int main() {
	int pos, cases, i;

	scanf("%d", &cases);

	for (i = 0; i < cases; i++) {
		scanf("%d", &pos);
		if (pos % 2 != 0) {
			printf("%d\n", pos / 2 + 1);
		} else {
			printf("%d\n", pos / 2);
		}
	}

	return 0;
}