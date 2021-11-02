const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});
const dgram = require('dgram')
const quem = 'cliente'
const server = dgram.createSocket('udp4');

server.on('error', (err) => {
  console.log(`server error:\n${err.stack}`);
  server.close();
});

server.on('message', (msg, rinfo) => {
  console.log(`server got: ${msg} from ${rinfo.address}:${rinfo.port}`);
});

function pedeCalculo() {
  rl.question("Digite um número\n", (num1) => {
		if (num1 == 'FIM') {
			process.exit()
		}
    rl.question("Digite um operando\n", (operando) => {
      rl.question("Digite outro número\n", (num2) => {
        const data = { num1, num2, operando, quem }
        server.send(JSON.stringify(data), 1972, 'localhost', (error) => {
          pedeCalculo()
        })
      })
    })
  });
}

server.on('listening', () => {
  const address = server.address();
  console.log(`server listening ${address.address}:${address.port}`);
  pedeCalculo()
});

server.bind(41232);