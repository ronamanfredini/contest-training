// var input = require('fs').readFileSync('/dev/stdin', 'utf8');
// var lines = input.split('\n');

var lines = [
	// "10 8",
	// "C 1234 5",
	// "C 1111 4",
	// "C 2222 4",
	// "C 4321 3",
	// "S 1111",
	// "C 2002 6",
	// "C 4321 3",
	"30 10",
	"C 1000 10",
	"C 1001 10",
	"C 1002 10",
	"S 1000",
	"S 1002",
	"C 1003 20",
	"S 1001",
	"C 1004 20",
	"S 1004",
	"C 1005 30",
	// "20 10",
	// "C 1234 20",
	// "C 5678 1",
	// "S 1234",
	// "C 1234 20",
	// "C 5678 1",
	// "S 1234",
	// "C 5678 1",
	// "C 1234 20",
	// "C 5555 1",
	// "S 5678"
];

function solution(lines) {
	var parkingPrice = 10;

	for (var i = 0; i < lines.length; i++) {
		var vals = lines[i].split(' ');
		var comprimento = parseInt(vals[0]);
		var eventosCount = parseInt(vals[1]);
		var estacionados = [];

		var comprimentoTotalPreenchido, faturamento;
		comprimentoTotalPreenchido = faturamento = 0;

		++i;
		for (j = 0; j < eventosCount; j++, i++) {
			var eventVals = lines[i].split(' ');
			var operationType = eventVals[0];
			var placa = eventVals[1];
			if (operationType == 'C') {
				var carLength = parseInt(eventVals[2]);

				if (carLength + comprimentoTotalPreenchido <= comprimento) {
                    
                    if (estacionados.length == 0) {
                        var car = {
							firstIndex: 0,
							lastIndex: carLength - 1;
                        };
                        estacionados.push(car);
                    } else {
                        for (var k = estacionados[0].lastIndex; k < estacionados.length; k++) {
                            if (estacionados)
                        }
                    }
                    
                    
				}
			} else if (operationType == 'S') {
				var car = estacionados.get(placa);
				comprimentoTotalPreenchido -=  car.lastIndex - car.firstIndex + 1;
				estacionados.delete(placa);
				faturamento += parkingPrice;
			}
		}
		i -= 2;
		faturamento += estacionados.size * parkingPrice;
	}
}
solution(lines);