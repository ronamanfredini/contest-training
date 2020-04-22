#include <iostream>
#include <map>
#include <vector>

#define VALOR_ESTACIONAMENTO 10

using namespace std;

struct carro {
	int indiceInicial;
	int comprimento;
};

int main() {
	int comprimentoEstacionamento, eventos, faturamento;

	while (cin >> comprimentoEstacionamento >> eventos) {
		faturamento = 0;
		map<int, carro> estacionados;
		map<int, carro>::iterator it;
		vector<int> estacionamento(comprimentoEstacionamento);
		fill(estacionamento.begin(), estacionamento.end(), 0);

		for (int i = 0; i < eventos; i++) {
			char eventoTipo;
			int placa;
			cin >> eventoTipo >> placa;
			if (eventoTipo == 'C') {
				int comprimentoCarro;
				cin >> comprimentoCarro;
				int first0Index = -1;
				for (int j = 0; j < comprimentoEstacionamento; j++) {
					if (estacionamento[j] == 0 && first0Index == -1) {
						first0Index = j;
					}

					//Encontrou uma posição não zero ou o final do vetor.
					if ((estacionamento[j] != 0 && first0Index != -1) || j == comprimentoEstacionamento - 1) {
						if (1 + j - first0Index >= comprimentoCarro) {
							 for (int k = first0Index; k < first0Index + comprimentoCarro; k++) {
								 estacionamento[k] = placa;
								 
							 }
							 pair<int, carro> identificadorCarro = pair<int, carro>(placa, {first0Index, comprimentoCarro});
							 estacionados.insert(identificadorCarro);
						}
					}
					if (estacionamento[j] != 0) {
						first0Index = -1;
					}
				}
			} else if (eventoTipo == 'S') {
				it = estacionados.find(placa);
				for (int j = it->second.indiceInicial; j < it->second.indiceInicial + it->second.comprimento; j++) {
					estacionamento[j] = 0;
				}
				faturamento += VALOR_ESTACIONAMENTO;
				estacionados.erase(it);
			}
		}

		faturamento += VALOR_ESTACIONAMENTO * estacionados.size();
		estacionados.clear();
		estacionamento.clear();
		cout << faturamento << endl;
	}
	return 0;
}