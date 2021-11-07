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
    const response = await callServer(base)
    console.log(`[${who}] --> Received data from SERVER`)
    return response
  }

  return {baseData: `Base ${base} is not alive. Aborting...`, status: false}
}

const dataFlow = async data => {
  if (data.type === 'status') {
    aliveInstances[data.baseNum] = { status: true, lastSeen: new Date().getTime(), port: data.port }
    console.log(aliveInstances)
    return 'Ok'
  } else if (data.type === 'data') {
    console.log(`[${who}] --> Calling SERVER for data from Base ${data.message}`)
    const response = await getData(data.message)
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
    const response = await dataFlow(dataAsJson)
    connection.write(dataHandler.encodeData(response))
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

setInterval(() => {
  for (const [key, value] of Object.entries(aliveInstances)) {
    if (value.lastSeen < new Date().getTime() - 2000) {
      console.log(`Stopped receiving status from Base ${key}. Removing from available servers.`)
      delete aliveInstances[key]
    }
  }
}, 1000)
