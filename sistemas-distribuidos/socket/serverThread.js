'use strict'

const { Worker, MessageChannel, MessagePort, isMainThread, parentPort } = require('worker_threads');
const dataHandler = require('./handlers/data')
const connectionHandler = require('./handlers/connection')
let communicationPort;
let savedConnection
let threadId

function doSetup(messagePort, id) {
  console.log(`Preparing thread ${id} for fetching data...`)
  communicationPort = messagePort
  threadId = id
}

async function getDatabase(data) {
  const formattedData = dataHandler.formatData(data.message.data)

  console.log(`THREAD #${threadId} --> Calling BASE #${formattedData.base} `)
  const response = await connectionHandler.doRequest(formattedData.port, {})

  const formattedResponse = {
    baseData: response,
    serverId: threadId
  }

  console.log(`THREAD #${threadId} --> Data fetched on BASE #${formattedData.base}`)
  return communicationPort.postMessage(formattedResponse)
}

parentPort.on('message', (value) => {
  if (value.messagePort instanceof MessagePort) {
    return doSetup(value.messagePort, value.id)
  }

  if (value.message.type == 'data') {
    return getDatabase(value)
  }
});
