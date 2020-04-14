#include <iostream>
#include <map>
#include <vector>

using namespace std;


int main() {
	int comprimento, eventos, comprimentoTotalPreenchido, faturamento;

	while (cin >> comprimento >> eventos) {
		map<int, int> estacionados;
		map<int, int>::iterator it;
		vector<int> estacionamento(comprimento);
		fill(estacionamento.begin(), estacionamento.end(), 0);

		comprimentoTotalPreenchido = faturamento = 0;
		for (int i = 0; i < eventos; i++) {
			char tipoEvento;
			int placa, comprimentoCarro;
			cin >> tipoEvento >> placa;

			if (tipoEvento == 'C') {
				cin >> comprimentoCarro;
				if (comprimentoCarro + comprimentoTotalPreenchido <= comprimento) {
					int first0Pos = -1;
					for (int i = 0; i < comprimento; i++) {
						if (first0Pos == -1 && estacionamento[i] == 0) {
							first0Pos = i;
						}

 						if ((estacionamento[i] != 0 || i + 1 == comprimento) && i - 1 - first0Pos > comprimentoCarro) {
							cout << "0pos - " << first0Pos<<endl;
							for (int j = first0Pos; j < i; j++) {
								estacionamento[j] = placa;
							}
							break;
						} else if (estacionamento[i] != 0) {
							first0Pos == -1;
						}
					}

					pair<int, int> par = pair<int,int>(placa, comprimentoCarro);
					estacionados.insert(par);
					comprimentoTotalPreenchido += comprimentoCarro;
				}
			} else if (tipoEvento == 'S') {
				it = estacionados.find(placa);
				if (it!=estacionados.end()) {
					faturamento += 10;
					comprimentoTotalPreenchido -= it->second;
					estacionados.erase(it);
				}
			}
			for (int j = 0; j < comprimento; j++) {
				cout<< j << " - " << estacionamento[j] << endl;
			}
		}

		for (it = estacionados.begin(); it != estacionados.end(); ++it) {
			faturamento += 10;
		}

		cout << faturamento << endl;
	}
}