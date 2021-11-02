const { Worker, MessageChannel } = require('worker_threads');

let services = []
let awaiters = {}
const serviceQtd = 10

function serviceMessageHandler(value) {
  awaiters[value.serverId](value)
}

function createServicePort(id) {
  const serverChannel = new MessageChannel();
  serverChannel.port2.on('message', serviceMessageHandler)

  return serverChannel.port1
}

function createService(id) {
  services[id] = new Worker('./server.js')
  const port = createServicePort(id)
  services[id].postMessage({ messagePort: port, serviceMessage: 'Serviço ' + id, id }, [port]);
}

function sendMessage(message, id) {
  return new Promise((resolve, reject) => {
    awaiters[id] = resolve
    services[id].postMessage({ message, type: 'message' })
  })
}

async function recursiveRetryOnError(message, id, timesTried = 0) {
  const result = await sendMessage(message, id)
  if (result.success) {
    return result.message
  }

  if (timesTried <= 5) {
    console.log(`Service ${id} failed. Retrying...`)
    return recursiveRetryOnError(message, id, ++timesTried)
  }
  throw new Error(`Service ${id} failed more than 5 times. System halted.`)
}

async function doMessageFlow(initial) {
  let message = initial
  for (let i = 0; i < serviceQtd; i++) {
    message = await recursiveRetryOnError(message, i)
  }

  return message
}

function main() {
  for (let i = 0; i < serviceQtd; i++) {
    createService(i)
  }
  createService()

  setTimeout(async () => {
    try {
      const message = await doMessageFlow('Início')
      console.log('Final Message -> ', message)
    } catch(err) {
      console.log('Error: ', err.message)
    }
  }, 1000)
}

main()