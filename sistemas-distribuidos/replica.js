const { MessagePort, parentPort } = require('worker_threads');
let communicationPort;
let serviceMessage;
let serverId;
let timeout

function doSetup(configData) {
	communicationPort = configData.messagePort
	serviceMessage = configData.serviceMessage
	serverId = configData.id
	timeout = configData.timeout
}

parentPort.on('message', (value) => {
	if (value.messagePort instanceof MessagePort) {
		return doSetup(value)
	}

	if (value.type == 'message') {
		console.log(timeout)
		if (timeout && timeout > 0) {
			setTimeout(() => {
				const formattedMessage = formatMessage(value.message)
				return communicationPort.postMessage(formattedMessage)
			}, timeout)
		}
	}
});


function formatMessage(message) {
	const splitted = message.split('+')
	return {serverId, value: parseInt(splitted[0]) + parseInt(splitted[1]) }
}