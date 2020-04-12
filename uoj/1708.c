#include <stdio.h>

int main() {

	int a, b, laps, secDiff;

	scanf("%d",&a); scanf("%d",&b);

	secDiff = b - a;
	laps = b / secDiff;

	if (b % secDiff != 0) {
		laps++;
	}
	printf("%d\n", laps);
	return 0;
}