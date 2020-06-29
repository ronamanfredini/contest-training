const {
    Worker, MessageChannel
} = require("worker_threads");
const { BaseMessage, MessageTypes } = require("./messageInterface.js");
const fs = require("fs");
const path = require("path");
const filePath = path.join(__dirname, "comm.txt");
const args = process.argv.slice(2);
const workerCount = parseInt(args[0]);

var workers = [];
var messageChannels = [];

function getDirection(actual, target) {
    let rightPath = Math.abs(actual - target);
    let leftPath = workerCount - target + actual;
    if (leftPath > workerCount) {
        leftPath = workerCount - (leftPath % workerCount);
    }
    if (rightPath <= leftPath) {
        return actual < target ? 1 : -1;
    }
    return actual <= workerCount / 2 ? -1 : 1;
}

function resolveSender(actual, target) {
    let nextSender = actual + getDirection(actual, target);
    if (nextSender == -1) return workerCount - 1;
    if (nextSender == workerCount) return 0;
    return nextSender;
}

function handleTransferMessage(data) {
    workers[resolveSender(data.actualSender, data.target)].postMessage(data);
}

function handleMessage(messageObj) {
    if (messageObj.type == MessageTypes.SUCCESS) console.log(messageObj.message);
    if (messageObj.type == MessageTypes.TRANSFER) handleTransferMessage(messageObj);
}

for (let i = 0; i < workerCount; i++) {
    workers[i] = new Worker("./worker.js", { argv: [i] });
    messageChannels[i] = new MessageChannel();

    let setupMessage = new BaseMessage();
    setupMessage.message = messageChannels[i].port1;
    setupMessage.type = MessageTypes.SETUP;
    workers[i].postMessage(setupMessage, [messageChannels[i].port1]);

    messageChannels[i].port2.on("message", handleMessage);
}

fs.readFile(filePath, { encoding: "utf-8" }, (err, data) => {
    let fileContents = data.split("\n").slice(1);
    for (let i = 0; i < fileContents.length; i++) {
        if (fileContents[i].length > 0) {
            let messageData = fileContents[i].split(',');
            let initialSender = parseInt(messageData[0]);
    
            let initialMessage = new BaseMessage();
            initialMessage.type = MessageTypes.START;
            initialMessage.message = messageData[2];
            initialMessage.originalSender = initialSender;
            initialMessage.actualSender = initialSender;
            initialMessage.target = parseInt(messageData[1]);
            workers[initialSender].postMessage(initialMessage);
        }
    }
});
