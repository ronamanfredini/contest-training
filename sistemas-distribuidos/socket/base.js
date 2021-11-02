//SERVER

console.log(process.argv)
const who = 'SERVER'
const net = require('net')
const dataHandler = require('./handlers/data')
const fs = require('fs');

const getParsedData = (baseCode, connection) => {
    const rawdata = fs.readFileSync(`base/base${baseCode}.json`);
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
    console.log(`end ${who}`)
  })

  connection.on('data', data => {
    const formattedData = dataHandler.formatData(data);
    if (formattedData.type == 'status')
        connection.write('to vivo')
    else {
        const parsedData = getParsedData(formattedData.message);
        connection.write(JSON.stringify(parsedData));
    }
    connection.pipe(connection);
  })
})


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
  port: 8100,
  exclusive: true
})