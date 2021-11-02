const dgram = require('dgram');

const server = dgram.createSocket('udp4');

server.on('error', (err) => {
  console.log(`server error:\n${err.stack}`);
  server.close();
});

server.on('message', (msg, rinfo) => {
  const parsedMessage = JSON.parse(msg)
  console.log('recebi de ' + parsedMessage.quem + ' do endereço ' + rinfo.address + ':' + rinfo.port + ' a mensagem: ' + msg)

  if (parsedMessage.quem == 'gerenciador') {
    return server.send('tô vivo', rinfo.port, rinfo.address, (err) => {

    })
  }

  let conta = ''
  parsedMessage.num1 = parseFloat(parsedMessage.num1)
  parsedMessage.num2 = parseFloat(parsedMessage.num2)

  if (parsedMessage.quem == 'cliente') {
    if (parsedMessage.operando == '-') {
      conta = `${(parsedMessage.num1 - parsedMessage.num2)}`
    }

    if (parsedMessage.operando == '+') {
      conta = parsedMessage.num1 + parsedMessage.num2
    }
    
    if (parsedMessage.operando == '/') {
      conta = `${(parsedMessage.num1 / parsedMessage.num2)}`
    }

    if (parsedMessage.operando == '*') {
      conta = `${(parsedMessage.num1 * parsedMessage.num2)}`
    }
  }

  server.send(conta.toString(), rinfo.port, rinfo.address, (err) => {

  })

});

server.on('listening', () => {
  const address = server.address();
  console.log(`server listening ${address.address}:${address.port}`);

});

server.bind(1972);
// Prints: server listening 0.0.0.0:41234