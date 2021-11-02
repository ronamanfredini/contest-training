//CLIENT
const who = 'CLIENT'
const net = require('net')
const dataHandler = require('./handlers/data')
const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

rl.question("De qual base você quer fazer backup?", (answer) => {
  const client = net.createConnection({ port: 8090 }, () => {
    console.log(`[${who}] --> Sucessfully connected to Manager`);

    const data = {
      message: answer,
      origin: who
    }

    client.write(dataHandler.encodeData(data))
  })

  client.on('data', (data) => {
    console.log(data.toString());
    client.end();
  })

  client.on('end', () => {
    console.log('disconnected from server');
  })
})

