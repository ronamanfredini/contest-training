#include <iostream>

using namespace std;

int main() {

	bool first[5], second[5];
	for (int i =0; i < 5; i++) {
		cin >> first[i];
		first[i] = !first[i];
	}
	for (int i =0; i < 5; i++) {
		cin >> second[i];
	}

	bool equal = true;
	for (int i =0; i < 5; i++) {
		if (first[i] != second[i]) {
			equal = false;
			break;
		}
	}
	if (equal)
		cout << "Y" << endl;
	else 
		cout << "N" << endl;
	return 0;
}