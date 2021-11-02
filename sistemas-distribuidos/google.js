const { Worker, MessageChannel, MessagePort, isMainThread, parentPort } = require('worker_threads');
console.log('google')


let communicationPort;

const users = {
  ronaldo: {
    password: '123456789',
    email: 'ronald677br@gmail.com'
  }
}

function doSetup(messagePort) {
  communicationPort = messagePort
  console.log('google configuration done!')
}

function doAuth(data) {
  if (!users[data.name]) {
    return communicationPort.postMessage('invalid auth')
  }

  if (users[data.name].password !== data.password) {
    return communicationPort.postMessage('invalid auth')
  }

  return communicationPort.postMessage(data)
}

parentPort.on('message', (value) => {
  if (value.messagePort instanceof MessagePort) {
    return doSetup(value.messagePort)
  }

  if (value.type == 'auth') {
    return doAuth(value)
  }
});

