//SERVER

const who = 'SERVER'
const net = require('net')
const dataHandler = require('./handlers/data')
const { Worker, MessageChannel, MessagePort, isMainThread, parentPort } = require('worker_threads');
let servicesId = 0

let services = []
let awaiters = {}

function serviceMessageHandler(value) {
  awaiters[value.serverId](value)
}
function createServicePort() {
  const serverChannel = new MessageChannel();
  serverChannel.port2.on('message', serviceMessageHandler)

  return serverChannel.port1
}

function sendMessage(message, id) {
  return new Promise((resolve, reject) => {
    awaiters[id] = resolve
    services[id].postMessage({ message, type: 'message' })
  })
}

function createService(id) {
  services[id] = new Worker('./serverThread.js')
  const port = createServicePort(id)
  services[id].postMessage({ messagePort: port, id, serviceMessage: 'Serviço ' + id, id }, [port]);
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
    const thisThreadId = ++servicesId
    createService(thisThreadId)
    const formattedData = await sendMessage({type: 'data', data}, thisThreadId)
    formattedData.origin = who
    console.log(`Received data from THREAD #${thisThreadId}`)

    connection.write(dataHandler.encodeData(formattedData))
    connection.pipe(connection)
  })
})


server.on('error', (e) => {
  if (e.code === 'EADDRINUSE') {
    console.log('Address in use, retrying...');
    setTimeout(() => {
      server.close();
      server.listen(8090, HOST);
    }, 1000);
  }
});

server.listen({
  host: 'localhost',
  port: 8090,
  exclusive: true
})