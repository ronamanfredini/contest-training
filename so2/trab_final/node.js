const { networkInterfaces } = require('os');
const express = require('express');
const app = express();
const port = 3001;
const http = require('https');
const nets = networkInterfaces();
const ips = [];

for (const name of Object.keys(nets)) {
	for (const net of nets[name]) {
		if (net.family === 'IPv4' && !net.internal) {
			ips.push(net.address);
		}
	}
}

app.get('/', (req, res) => {
	res.send('Hello World!');
});

app.listen(port, () => {
	console.log(`Example app listening at http://localhost:${port}`);
});

app.get('/status', (req, res) => {
	res.send({
		status: true,
		ip:ips[0]
	});

});



