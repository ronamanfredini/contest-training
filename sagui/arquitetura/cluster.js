const {
    Worker, MessageChannel, MessagePort, isMainThread, parentPort
} = require('worker_threads');

let MessageInterface = require('./messageInterface');
const args = process.argv.slice(2);
const workerCount = args[0];
var workers = [];


var subChannel = new MessageChannel();
subChannel.port1

for (let i = 1; i <= workerCount; i++) {
    workers[i] = new Worker('./worker.js', {argv: [i]});
}
