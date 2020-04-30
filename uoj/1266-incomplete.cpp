#include <iostream>
#include <vector>

using namespace std;

int main () {
	int cases;


	while (cin >> cases) {
		vector<int> postes;
		if (cases ==0)
			break;

		int metros = 0;
		int posteQtd = 0;
		for (int i = 0; i < cases; i++) {
			int poste;
			cin >> poste;
			postes.push_back(poste);
		}

		if (postes[0] == 0 && postes[postes.size() - 1] == 0 && postes[postes.size() - 2] != 0) {
			postes[0] = 1; posteQtd++;
		}
		for (int i = 0; i < postes.size(); i++) {
			int poste = postes[i];
			if (poste == 0) {
				metros += 2;
			} else {
				metros = 0;
			}

			if (metros == 4) {
				posteQtd++;
				postes[i] = 1;
				metros = 0;
			}
		}
		if (postes[0] == 0 && postes[postes.size() - 1] == 0) {
			postes[0] = 1; posteQtd++;
		}
		cout << posteQtd << endl;
	}

	
	return 0;
}