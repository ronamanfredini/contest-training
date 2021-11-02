//SERVER

const who = 'SERVER'
const net = require('net')
const dataHandler = require('./handlers/data')
const connectionHandler = require('./handlers/connection')

const server = net.createServer(connection => {
  connection.on('connect', data => {
    console.log(`close ${who}`)
  })

  connection.on('error', data => {
    console.log(`error ${who}`)
  })
  connection.on('end', data => {
  })

  connection.on('data', async data => {
    const formattedData = dataHandler.formatData(data)
    console.log(`[${who}] --> Calling BASE ${data.base}`)
    const response = await connectionHandler.doRequest(formattedData.port, {})

    console.log(response)
    const formattedResponse = {
      baseData: response,
      origin: who
    }

    connection.write(dataHandler.encodeData(formattedResponse))
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
  port: 8090,
  exclusive: true
})