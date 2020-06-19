const { BaseMessage, MessageTypes } = require('./messageInterface.js');
const { parentPort } = require('worker_threads');

const args = process.argv.slice(2);
const workerId = parseInt(args[0]);
var messagePort = undefined;

function setupWorker(data) {
    messagePort = data.message;
}

function handleTransferMessage(data) {
    let messageToSend = new BaseMessage();
    messageToSend.target = data.target;
    messageToSend.originalSender = data.originalSender;
    messageToSend.message = data.message;
    messageToSend.actualSender = workerId;

    if (data.message == workerId) {
        messageToSend.type = MessageTypes.SUCCESS;
        messageToSend.message = `Worker ${workerId} recebeu com sucesso a mensagem ${data.message}, vinda do Worker ${data.originalSender}`;
        messagePort.postMessage(messageToSend);
    } else {
        messageToSend.type = MessageTypes.TRANSFER;
        messagePort.postMessage(messageToSend);
    }
}

function handleMessage(messageObj) {
    if (messageObj.type == MessageTypes.SETUP && messagePort === undefined) setupWorker(messageObj);
    else if (messageObj.type == MessageTypes.TRANSFER) handleTransferMessage(messageObj);
}



parentPort.once("message", handleMessage);