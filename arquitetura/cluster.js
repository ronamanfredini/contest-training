const {
    Worker, MessageChannel
} = require('worker_threads');
const { BaseMessage, MessageTypes } = require('./messageInterface.js');

const args = process.argv.slice(2);
const workerCount = parseInt(args[0]);
const initialSender = parseInt(args[1])

var initialMessage = new BaseMessage();
initialMessage.type = MessageTypes.START;
initialMessage.message = args[3];
initialMessage.originalSender = initialSender;
initialMessage.actualSender = initialSender;
initialMessage.target = parseInt(args[2]);

var workers = [];
var messageChannels = [];

function getDirection(actual, target) {
    let rightPath = Math.abs(actual -  target);
    let leftPath  = workerCount - target + actual;
    if (leftPath > workerCount) {
        leftPath = workerCount - (leftPath % workerCount);
    }
    if (rightPath <= leftPath) {
        return actual < target? 1: -1;
    }
    return actual <= workerCount / 2? -1: 1;
}

function resolveSender(actual, target) {
    let nextSender = actual + getDirection(actual, target);
    if (nextSender == 0) return workerCount;
    if (nextSender == workerCount + 1) return 1;
    return nextSender;
}

function handleTransferMessage(data) {
    workers[resolveSender(data.actualSender, data.target)].postMessage(data);
}

function handleMessage(messageObj) {
    if (messageObj.type == MessageTypes.SUCCESS) console.log(messageObj.message);
    if (messageObj.type == MessageTypes.TRANSFER) handleTransferMessage(messageObj);
}

for (let i = 1; i <= workerCount; i++) {
    workers[i] = new Worker("./worker.js", {argv: [i]});
    messageChannels[i] = new MessageChannel();

    let setupMessage = new BaseMessage();
    setupMessage.message = messageChannels[i].port1;
    setupMessage.type = MessageTypes.SETUP;
    workers[i].postMessage(setupMessage, [messageChannels[i].port1]);

    messageChannels[i].port2.on("message", handleMessage);
}

workers[initialSender].postMessage(initialMessage);