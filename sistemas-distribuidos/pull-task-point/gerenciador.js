const dgram = require('dgram')

const quem = 'gerenciador'
const server = dgram.createSocket('udp4');

server.on('error', (err) => {
	console.log(`server error:\n${err.stack}`);
	server.close();
});

server.on('message', (msg, rinfo) => {
	console.log(`server got: ${msg} from ${rinfo.address}:${rinfo.port}`);
});

server.on('listening', () => {
	const address = server.address();
	console.log(`server listening ${address.address}:${address.port}`);
});

setInterval(() => {
	server.send(JSON.stringify({ quem }), 1972, 'localhost', (error) => {
	})
}, 1000)
server.bind(41234);
// Prints: server listening 0.0.0.0:41234