//MANAGER
const who = 'MANAGER'
const net = require('net')
const dataHandler = require('./handlers/data')

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
    const parsedData = dataHandler.formatData(data)
    console.log(`[${who}] --> Received data from ${parsedData.origin}`)

    connection.write('resposta')
    connection.pipe(connection)
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
  port: 8070,
  exclusive: true
})
