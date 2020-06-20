const { MessageTypes } = require('./messageInterface.js');
const { parentPort } = require('worker_threads');

const args = process.argv.slice(2);
const workerId = parseInt(args[0]);
var messagePort = undefined;

function setupWorker(data) {
    messagePort = data.message;
}

function handleTransferMessage(data) {
    console.log(`Worker ${workerId} recebeu com sucesso a mensagem ${data.message}, vinda do Worker ${data.actualSender} com destino ao Worker ${data.target}`);
    data.actualSender = workerId;
    if (data.target == workerId) {
        data.type = MessageTypes.SUCCESS;
        data.message = `Mensagem chegou ao destino`;
    }
    messagePort.postMessage(data);
}

function handleMessage(messageObj) {
    if (messageObj.type == MessageTypes.SETUP && messagePort === undefined) setupWorker(messageObj);
    else if (messageObj.type == MessageTypes.TRANSFER){ handleTransferMessage(messageObj); };
}

parentPort.on("message", handleMessage);