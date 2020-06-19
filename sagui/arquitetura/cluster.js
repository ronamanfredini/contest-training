const {
    Worker, MessageChannel
} = require('worker_threads');
const { BaseMessage, MessageTypes } = require('./messageInterface.js');

const args = process.argv.slice(2);
const workerCount = args[0];
var workers = [];
var messageChannels = [];

function handleTransferMessage(data) {
    let routeLeft = data.actualSender;
}

function handleMessage(messageObj) {
    if (messageObj.type == MessageTypes.SUCCESS) console.log(messageObj.message);
    if (message.type == MessageTypes.TRANSFER) handleTransferMessage(messageObj);
}


for (let i = 1; i <= workerCount; i++) {
    workers[i] = new Worker('./worker.js', {argv: [i]});
    messageChannels[i] = new MessageChannel();

    let setupMessage = new BaseMessage();
    setupMessage.message = messageChannels[i].port1;
    setupMessage.type = MessageTypes.SETUP;
    workers[i].postMessage(setupMessage, [messageChannels[i].port1]);

    messageChannels[i].port2.on("message", handleMessage);
}


