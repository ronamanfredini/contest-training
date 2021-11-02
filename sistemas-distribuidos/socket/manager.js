//MANAGER
const who = 'MANAGER'
const net = require('net')
const dataHandler = require('./handlers/data')
const connectionHandler = require('./handlers/connection')
const aliveInstances = {}

const validateAliveBase = base => aliveInstances[base] && new Date().getTime() < aliveInstances[base].lastSeen + 10000
const getBasePort = base => aliveInstances[base].port
const callServer = base => {
  return connectionHandler.doRequest(8090, { base, origin: who, port: getBasePort(base) })
}

const getData = async (base) => {
  if (validateAliveBase(base)) {
    return await callServer(base)
  }

  return `Base ${base} is not alive. Aborting...`
}

const dataFlow = async data => {
  if (data.type === 'status') {
    aliveInstances[data.baseNum] = { status: true, lastSeen: new Date().getTime(), port: data.port }
    console.log(aliveInstances)
    return 'Ok'
  } else if (data.type === 'data') {
    console.log(`[${who}] --> Calling SERVER for data from Base ${data.message}`)
    const response = await getData(data.message)
    console.log(`[${who}] --> Received data from ${response.origin} ${response.message}`)
    return dataHandler.formatData(dataHandler.encodeData(response))
  }
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

  connection.on('data', async data => {
    const dataAsJson = dataHandler.formatData(data)
    console.log(`[${who}] --> Received data from ${dataAsJson.origin}`)
    const response = await dataFlow(dataAsJson)
    connection.write(response)
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
