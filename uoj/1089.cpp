#include <iostream>
using namespace std;

int main() {
	int casos;

	while(cin >> casos) {
		if (casos == 0) {
			break;
		}

		int coordinates[casos];
		for (int i = 0; i < casos; i++) {
			int caso;
			cin >> caso;
			coordinates[i] = caso;
		}
		int peaks = 0;
		for (int i = 1; i < casos - 1; i++) {
			if (!(coordinates[i - 1] < coordinates[i] && coordinates[i] < coordinates[i + 1] || coordinates[i - 1] > coordinates[i] && coordinates[i] > coordinates[i + 1]))
				peaks++;
		}
		cout << peaks << endl;
	}


	return 0;
}