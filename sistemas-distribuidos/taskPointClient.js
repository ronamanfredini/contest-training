const { Worker, MessageChannel } = require('worker_threads');

let services = []
let awaiters = {}

function serviceMessageHandler(value) {
	awaiters[value.serverId](value)
}

function createServicePort() {
	const serverChannel = new MessageChannel();
	serverChannel.port2.on('message', serviceMessageHandler)

	return serverChannel.port1
}

function createService(id) {
	services[id] = new Worker('./taskPointServer.js')
	const port = createServicePort()
	services[id].postMessage({ messagePort: port, serviceMessage: 'Serviço ' + id, id }, [port]);
}

function sendMessage(message, id) {
	return new Promise((resolve, reject) => {
		awaiters[id] = resolve
		services[id].postMessage({ message, type: 'message' })
	})
}

function main() {
	createService(1)

	setTimeout(async () => {
		try {
			const message = await sendMessage('2+2', 1)

			console.log('Final Message -> ', message)
		} catch (err) {
			console.log('Error: ', err.message)
		}
	}, 1000)
}

main()
