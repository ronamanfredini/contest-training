const { MessagePort, parentPort } = require('worker_threads');

let communicationPort;
let serviceMessage;
let serverId;

function doSetup(configData) {
  communicationPort = configData.messagePort
  serviceMessage = configData.serviceMessage
  serverId = configData.id
}

parentPort.on('message', (value) => {
  if (value.messagePort instanceof MessagePort) {
    return doSetup(value)
  }

  if (value.type == 'message') {
    const formattedMessage = formatMessage(value.message)
    return communicationPort.postMessage(formattedMessage)
  }
});

function formatMessage(message) {
  const success = getRandomInt(0, 10) % 3 == 0
  if (!success) {
    return { serverId, success }
  }
  return { message: `${message} ${serviceMessage}`, serverId, success }
}

function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min + 1)) + min;
}