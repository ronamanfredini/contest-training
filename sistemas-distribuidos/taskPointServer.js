const { MessagePort, parentPort } = require('worker_threads');
const { Worker, MessageChannel } = require('worker_threads');

const invert  = p  => new Promise((res, rej) => p.then(rej, res));
const firstOf = ps => invert(Promise.all(ps.map(invert)));

let services = []
let awaiters = {}
const serviceQtd = 2

let communicationPort;
let serviceMessage;
let serverId;

function serviceMessageHandler(value) {
	awaiters[value.serverId](value)
}

function createServicePort(id) {
	const serverChannel = new MessageChannel();
	serverChannel.port2.on('message', serviceMessageHandler)

	return serverChannel.port1
}

function createService(id) {
	services[id] = new Worker('./replica.js')
	const port = createServicePort(id)
	if (id == 1) {
		services[id].postMessage({ messagePort: port, serviceMessage: 'Serviço ' + id, timeout: 1000, id }, [port]);
	} else {
		services[id].postMessage({ messagePort: port, serviceMessage: 'Serviço ' + id, id }, [port]);
	}
}


function doSetup(configData) {
	communicationPort = configData.messagePort
	serviceMessage = configData.serviceMessage
	serverId = configData.id
	for (let i = 0; i < serviceQtd; i++) {
		createService(i)
	}
}

parentPort.on('message', async (value) => {
	if (value.messagePort instanceof MessagePort) {
		return doSetup(value)
	}

	if (value.type == 'message') {
		const formattedMessage = await firstOf([sendMessage(value.message, 1), sendMessage(value.message, 2)])
		return communicationPort.postMessage(formattedMessage)
	}
});

function sendMessage(message, id) {
	return new Promise((resolve, reject) => {
		awaiters[id] = resolve
		services[id].postMessage({ message, type: 'message' })
	})
}

function formatMessage(message) {
	return { message, serverId, }
}

function getRandomInt(min, max) {
	min = Math.ceil(min);
	max = Math.floor(max);
	return Math.floor(Math.random() * (max - min + 1)) + min;
}