const {
    MessageChannel, MessagePort, parentPort
} = require('worker_threads');

const args = process.argv.slice(2);
const workerId = parseInt(args[0]);

parentPort.once("message", (message) => console.log(message));
console.log(workerId);
