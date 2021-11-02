//SERVER

const port = process.argv[2]
const baseNum = process.argv[3]
const connectionHandler = require('./handlers/connection')
const who = 'SERVER'
const net = require('net')
const fs = require('fs');

const getParsedData = () => {
    const rawdata = fs.readFileSync(`base/base${baseNum}.json`);
    return JSON.parse(rawdata);
}

const server = net.createServer(connection => {
  connection.on('connect', data => {
    console.log(`close ${who}`)
  })

  connection.on('error', data => {
    console.log(`error ${who}`)
  })
  connection.on('end', data => {
  })

  connection.on('data', () => {
    const parsedData = getParsedData();
    connection.write(JSON.stringify(parsedData));
    connection.pipe(connection);
  })
})


setInterval(() => {
  connectionHandler.doRequest(8070, { type: 'status', port, baseNum, origin: 'BASE' })
}, 1000)

server.on('error', (e) => {
  if (e.code === 'EADDRINUSE') {
    console.log('Address in use, retrying...');
    setTimeout(() => {
      server.close();
      server.listen(PORT, HOST);
    }, 1000);
  }
});

server.listen({
  host: 'localhost',
  port,
  exclusive: true
})